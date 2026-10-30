"""Guard public onboarding images and their board/secret boundaries."""
import argparse
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import tarfile
import tempfile
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('web_build', ROOT / 'scripts/build_web_firmware.py')
web_build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(web_build)


class WebFirmwareTest(unittest.TestCase):
    def test_factory_images_are_only_provisioning(self):
        for slug in web_build.PROFILES:
            text = (ROOT / f'firmware/factory/esp32-{slug}.yaml').read_text()
            web_build.verify_factory_source(text)
            self.assertIn(f'/firmware/adopt/esp32-{slug}.yaml@${{release_version}}', text)
            self.assertIn('hardware_uart: UART0', text)

    def test_functional_or_secret_inputs_are_rejected(self):
        valid = 'improv_serial:\ndashboard_import:\nname_add_mac_suffix: true\n'
        for extra in ('password: bad', '  key: bad', 'zwave_proxy:', 'ota:', 'packages:', 'wifi: !secret wifi'):
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                web_build.verify_factory_source(valid + extra)

    def test_exact_board_catalog_and_factory_offset(self):
        catalog = json.loads((ROOT / 'web-flasher.json').read_text())
        self.assertEqual({p['id'] for p in catalog['profiles']}, {'wroom', 's3'})
        for profile in catalog['profiles']:
            self.assertEqual(profile['chip_family'], web_build.PROFILES[profile['id']][0])
            self.assertEqual(profile['parts'], [{'path': f"firmware/zac93-{profile['id']}.factory.bin", 'offset': 0}])
            self.assertEqual(profile['provisioning'], 'improv')

    def test_adopted_application_retains_encrypted_ota(self):
        for slug in web_build.PROFILES:
            text = (ROOT / f'firmware/adopt/esp32-{slug}.yaml').read_text()
            self.assertNotIn('!secret', text)
            self.assertIn('key: REPLACE_WITH_YOUR_UNIQUE_32_BYTE_BASE64_KEY', text)
            self.assertEqual(text.count('encryption: {}'), 1)
            self.assertIn('radio: !include ../radio.yaml', text)

    def test_source_archive_has_rebuild_inputs_and_excludes_binary_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            package = work / 'installed' / 'esphome'
            package.mkdir(parents=True)
            (package / 'core.cpp').write_text('// matching runtime source')
            license_path = work / 'installed' / 'esphome.dist-info' / 'licenses' / 'LICENSE'
            license_path.parent.mkdir(parents=True)
            license_path.write_text('Runtime license notice')
            for slug in web_build.PROFILES:
                project = work / '.esphome' / 'build' / f'zac93-{slug}'
                (project / 'src').mkdir(parents=True)
                (project / 'src/main.cpp').write_text('// public factory source')
                (project / 'src/firmware.bin').write_bytes(b'exclude binary')
                (project / '.pioenvs').mkdir()
                (project / '.pioenvs/cache.bin').write_bytes(b'exclude build cache')
                (project / 'platformio.ini').write_text('[env]')
            dist = SimpleNamespace(files=['esphome.dist-info/licenses/LICENSE'],
                                   locate_file=lambda name: work / 'installed' / name)
            with patch.object(web_build.importlib.metadata, 'distribution', return_value=dist):
                web_build.archive_sources(work / 'sources.tar.gz', work)
            with tarfile.open(work / 'sources.tar.gz') as archive:
                names = set(archive.getnames())
            self.assertIn('esphome/core.cpp', names)
            self.assertIn('licenses/0-LICENSE', names)
            for slug in web_build.PROFILES:
                self.assertIn(f'firmware/factory/esp32-{slug}.yaml', names)
                self.assertIn(f'firmware/adopt/esp32-{slug}.yaml', names)
                self.assertIn(f'generated/{slug}/src/main.cpp', names)
            for name in ('web-flasher.json', 'firmware/radio.yaml', 'scripts/build_web_firmware.py', 'requirements.txt'):
                self.assertIn(name, names)
            self.assertFalse(any(name.endswith('.bin') or '.pioenvs' in name for name in names))

    def test_source_archive_refuses_missing_license(self):
        dist = SimpleNamespace(files=[], locate_file=lambda name: Path(name))
        with patch.object(web_build.importlib.metadata, 'distribution', return_value=dist):
            with self.assertRaisesRegex(ValueError, 'license is missing'):
                web_build.archive_sources(Path('unused.tar.gz'), Path('unused'))

    def test_version_cannot_inject_package_url(self):
        for value in ('../main', 'branch/name', 'x\nssid: bad', ''):
            with self.subTest(value=value), self.assertRaises(argparse.ArgumentTypeError):
                web_build.release_version(value)


if __name__ == '__main__':
    unittest.main()
