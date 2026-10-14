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
        for name in ('common.yaml', 'esp32-wroom.yaml', 'esp32-s3.yaml'):
            shutil.copyfile(root / 'firmware' / name, work / name)
        key = base64.b64encode(secrets.token_bytes(32)).decode()
        password = secrets.token_hex(24)
        (work / 'secrets.yaml').write_text(
            'wifi_ssid: "TEST_ONLY_NOT_A_REAL_NETWORK"\n'
            f'wifi_password: "{password}"\n'
            f'api_encryption_key: "{key}"\n'
            f'ota_password: "{password}"\n'
        )
        for name in ('esp32-wroom.yaml', 'esp32-s3.yaml'):
            for operation in operations:
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
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
