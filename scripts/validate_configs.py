#!/usr/bin/env python3
"""Validate, optionally compile, both boards with disposable test-only secrets."""
import argparse
import base64
from pathlib import Path
import secrets
import shutil
import subprocess
import sys
import tempfile


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compile', action='store_true', help='Also compile; never flash')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    operations = ['config', 'compile'] if args.compile else ['config']
    with tempfile.TemporaryDirectory(prefix='zac93-check-') as directory:
        work = Path(directory)
        for name in ('common.yaml', 'radio.yaml', 'esp32-wroom.yaml', 'esp32-s3.yaml'):
            shutil.copyfile(root / 'firmware' / name, work / name)
        (work / 'adopt').mkdir()
        for name in ('esp32-wroom.yaml', 'esp32-s3.yaml'):
            shutil.copyfile(root / 'firmware' / 'adopt' / name, work / 'adopt' / name)
        key = base64.b64encode(secrets.token_bytes(32)).decode()
        password = secrets.token_hex(24)
        (work / 'secrets.yaml').touch(mode=0o600)
        (work / 'secrets.yaml').write_text(
            'wifi_ssid: "TEST_ONLY_NOT_A_REAL_NETWORK"\n'
            f'wifi_password: "{password}"\n'
            f'api_encryption_key: "{key}"\n'
        )
        # Exercise the pinned ESPHome validator, not a local imitation of its schema.
        secrets_path = work / 'secrets.yaml'
        original_secrets = secrets_path.read_text()
        common_path = work / 'common.yaml'
        original_common = common_path.read_text()
        invalid_key = base64.b64encode(secrets.token_bytes(31)).decode()
        for case in ('short-key', 'password-with-encryption'):
            if case == 'short-key':
                secrets_path.write_text(original_secrets.replace(key, invalid_key))
            else:
                common_path.write_text(original_common.replace(
                    '    encryption: {}', '    encryption: {}\n    password: !secret wifi_password'))
            result = subprocess.run(
                [sys.executable, '-m', 'esphome', 'config', str(work / 'esp32-wroom.yaml')],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False,
            )
            # These assertions distinguish an intended schema rejection from e.g.
            # a missing dependency; never print the validation output or test keys.
            expected = '32' if case == 'short-key' else 'cannot be combined'
            if result.returncode == 0 or expected not in result.stdout:
                print(f'FAIL: expected schema rejection for {case}', flush=True)
                return 1
            print(f'PASS: schema rejects {case}', flush=True)
            secrets_path.write_text(original_secrets)
            common_path.write_text(original_common)
        for slug in ('wroom', 's3'):
            (work / f'adopt-{slug}.yaml').write_text(
                f'packages:\n  project: !include adopt/esp32-{slug}.yaml\n'
                f'api:\n  encryption:\n    key: {key}\n'
                'wifi:\n  ssid: TEST_ONLY_NOT_A_REAL_NETWORK\n'
                f'  password: {password}\n'
            )
        for name in ('esp32-wroom.yaml', 'esp32-s3.yaml', 'adopt-wroom.yaml', 'adopt-s3.yaml'):
            selected_operations = operations if not name.startswith('adopt-') else ['config']
            for operation in selected_operations:
                print(f'{name}: {operation}', flush=True)
                log = work / 'check.log'
                with log.open('w') as output:
                    result = subprocess.run(
                        [sys.executable, '-m', 'esphome', operation, str(work / name)],
                        stdout=output, stderr=subprocess.STDOUT, check=False,
                    )
                if result.returncode:
                    # Even disposable keys do not need to appear in CI output.
                    text = log.read_text(errors='replace').replace(key, '<redacted>')
                    text = text.replace(password, '<redacted>')
                    print('\n'.join(text.replace('\r', '\n').splitlines()[-60:]))
                    return result.returncode
                print('PASS', flush=True)
        # Valid adopted wrappers above differ from these only by the API key.
        # This proves a missing/generated-invalid key cannot publish a working
        # plaintext Z-Wave proxy accidentally.
        for slug in ('wroom', 's3'):
            valid = (work / f'adopt-{slug}.yaml').read_text()
            for case, text in (
                ('missing-key', valid.replace(f'api:\n  encryption:\n    key: {key}\n', '')),
                ('invalid-key', valid.replace(key, 'not-a-valid-base64-key')),
            ):
                config = work / f'adopt-{slug}-{case}.yaml'
                config.write_text(text)
                result = subprocess.run(
                    [sys.executable, '-m', 'esphome', 'config', str(config)],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
                )
                if result.returncode == 0:
                    print(f'FAIL: {slug} {case} was accepted', flush=True)
                    return 1
                print(f'PASS: {slug} {case} rejected', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
