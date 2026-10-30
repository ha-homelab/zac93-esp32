#!/usr/bin/env python3
"""Build credential-free USB onboarding images; never open a serial port."""
import argparse
import hashlib
import importlib.metadata
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {
    'wroom': ('ESP32', 'ESP32-WROOM-32/32D/32E DevKit, 4 MB', 4 * 1024**2),
    's3': ('ESP32-S3', 'ESP32-S3-DevKitC-1 N8, 8 MB', 8 * 1024**2),
}


def source_revision() -> str:
    """Use the checkout revision, or the pinned revision in a source archive."""
    try:
        top = subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'], cwd=ROOT,
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
        if Path(top).resolve() != ROOT.resolve():
            raise ValueError('Archive is nested in another checkout')
        revision = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True,
        ).strip()
    except (subprocess.CalledProcessError, ValueError):
        revision = (ROOT / 'SOURCE_REVISION').read_text().strip()
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('SOURCE_REVISION must be a full Git commit SHA')
    return revision


def archive_sources(output: Path, work: Path, revision: str) -> None:
    """Keep generated runtime sources and their upstream notices with binaries."""
    distribution = importlib.metadata.distribution('esphome')
    package = Path(distribution.locate_file('esphome'))
    roots = [(package, 'esphome')]
    licenses = [Path(distribution.locate_file(f)) for f in distribution.files or []
                if 'license' in Path(str(f)).name.lower() and '.dist-info/' in str(f)]
    if not licenses:
        raise ValueError('ESPHome distribution license is missing')
    roots.extend((p, f'licenses/{i}-{p.name}') for i, p in enumerate(licenses))
    for slug in PROFILES:
        project = work / '.esphome' / 'build' / f'zac93-{slug}'
        for path in project.iterdir():
            if path.name in {'src', 'components', 'managed_components'} or path.is_file():
                roots.append((path, f'generated/{slug}/{path.name}'))
    # Enumerate public source files: never walk the primary checkout, which may
    # contain ignored personal YAML or firmware.
    public_files = [
        'requirements.txt', 'scripts/build_web_firmware.py', 'scripts/validate_configs.py',
        'LICENSE', 'README.md', 'web-flasher.json', 'docs/browser-install.md',
        'firmware/common.yaml', 'firmware/radio.yaml', 'firmware/secrets.example.yaml',
    ]
    for slug in PROFILES:
        public_files.extend((f'firmware/esp32-{slug}.yaml',
                             f'firmware/adopt/esp32-{slug}.yaml',
                             f'firmware/factory/esp32-{slug}.yaml'))
    roots.extend((ROOT / p, p) for p in public_files)
    total = 0
    with tarfile.open(output, 'w:gz') as archive:
        revision_data = (revision + '\n').encode('ascii')
        info = tarfile.TarInfo('SOURCE_REVISION')
        info.size = len(revision_data)
        info.mode = 0o644
        archive.addfile(info, io.BytesIO(revision_data))
        for base, prefix in roots:
            candidates = sorted(base.rglob('*')) if base.is_dir() else [base]
            for path in candidates:
                if path.is_symlink():
                    raise ValueError('Source archive refuses symlinks')
                if not path.is_file() or '__pycache__' in path.parts or path.suffix in {'.pyc', '.bin', '.elf', '.o', '.a', '.log'}:
                    continue
                total += path.stat().st_size
                if total > 128 * 1024**2:
                    raise ValueError('Source archive exceeds 128 MiB input limit')
                name = str(Path(prefix) / path.relative_to(base)) if base.is_dir() else prefix
                archive.add(path, arcname=name, recursive=False)


def release_version(value: str) -> str:
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,79}', value):
        raise argparse.ArgumentTypeError('Use a release tag without slashes or whitespace')
    return value


def verify_factory_source(text: str) -> None:
    # These are bootstraps, never a user's functional controller or test build.
    if re.search(r'!secret|!include|^\s*(?:ssid|password|key|zwave_proxy|ota|external_components|packages|includes)\s*:', text, re.M):
        raise ValueError('Factory source includes credentials, a radio, OTA, or external inputs')
    for field in ('improv_serial:', 'dashboard_import:', 'name_add_mac_suffix: true'):
        if field not in text:
            raise ValueError(f'Factory source is missing {field}')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', type=release_version, required=True)
    parser.add_argument('--channel', choices=('stable', 'beta', 'rc', 'nightly'), default='beta')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--config-only', action='store_true')
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output must be a new directory')
    catalog = json.loads((ROOT / 'web-flasher.json').read_text())
    catalog['version'] = args.version
    catalog['channel'] = args.channel
    catalog['release_url'] = f'https://github.com/ha-homelab/zac93-esp32/releases/tag/{args.version}'
    for profile in catalog['profiles']:
        profile['setup_url'] = f'https://github.com/ha-homelab/zac93-esp32/blob/{args.version}/docs/browser-install.md#finish-secure-setup'
    revision = source_revision()
    records = []
    with tempfile.TemporaryDirectory(prefix='zac93-factory-') as directory:
        work = Path(directory)
        for slug, (chip, board, limit) in PROFILES.items():
            source = ROOT / 'firmware' / 'factory' / f'esp32-{slug}.yaml'
            text = source.read_text()
            verify_factory_source(text)
            config = work / source.name
            config.write_text(text)
            command = [sys.executable, '-m', 'esphome', '-s', 'release_version', args.version,
                       'config' if args.config_only else 'compile', str(config)]
            subprocess.run(command, check=True)
            if args.config_only:
                continue
            images = list((work / '.esphome' / 'build' / f'zac93-{slug}').glob('**/firmware.factory.bin'))
            if len(images) != 1:
                raise ValueError(f'Expected one factory image for {slug}, found {len(images)}')
            data = images[0].read_bytes()
            if not 65536 <= len(data) <= limit:
                raise ValueError(f'Unexpected factory image size for {slug}')
            records.append({'id': slug, 'chip_family': chip, 'board': board,
                            'path': f'firmware/zac93-{slug}.factory.bin',
                            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)})
        if args.config_only:
            print('PASS: both factory configurations validated; no output or flashing')
            return 0
        # Publish only after both compilations pass; no private YAML is copied.
        args.output.mkdir(parents=True)
        (args.output / 'firmware').mkdir()
        for record in records:
            image = next((work / '.esphome' / 'build' / f"zac93-{record['id']}").glob('**/firmware.factory.bin'))
            shutil.copyfile(image, args.output / record['path'])
            profile = next(p for p in catalog['profiles'] if p['id'] == record['id'])
            profile['parts'][0]['sha256'] = record['sha256']
        (args.output / 'web-flasher.json').write_text(json.dumps(catalog, indent=2) + '\n')
        (args.output / 'firmware-metadata.json').write_text(json.dumps({
            'source_commit': revision,
            'version': args.version, 'purpose': 'USB onboarding only; no radio or OTA',
            'esphome_requirement': (ROOT / 'requirements.txt').read_text().strip(),
            'images': records,
        }, indent=2) + '\n')
        archive_sources(args.output / 'firmware-sources.tar.gz', work, revision)
        (args.output / 'FIRMWARE-SOURCES.md').write_text(
            '# Firmware source and licenses\n\n'
            'The configuration and project scripts retain the repository MIT license. '
            'ESPHome C++ runtime is GPLv3; its Python tooling is MIT. '
            'The matching ESPHome package, license notices, generated runtime source, '
            'project manifests and public factory configurations are in firmware-sources.tar.gz. '
            'ESP-IDF and its bundled components retain their upstream licenses; '
            'their dependency versions are recorded in the generated project manifests.\n\n'
            'Install the pinned requirements.txt, then rebuild with python scripts/build_web_firmware.py '
            f'--version {args.version} --channel {args.channel} --output NEW_DIRECTORY. '
            'SOURCE_REVISION records the original Git commit when rebuilding outside a checkout. '
            'The normal ESPHome toolchain fetches its pinned ESP-IDF dependencies. '
            'This package preserves corresponding sources; it does not promise bit-for-bit reproduction. '
            'No signed boot restriction is added by this project.\n'
        )
        (args.output / 'SHA256SUMS').write_text(''.join(f"{r['sha256']}  {r['path']}\n" for r in records))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
