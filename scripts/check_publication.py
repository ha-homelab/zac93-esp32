#!/usr/bin/env python3
"""Reject private artifacts and literal credentials in the Git index.

Inspect staged blobs, not worktree content. Never print a matched secret.
Gitleaks complements this narrow file/configuration policy with content scanning.
"""
from pathlib import PurePosixPath
import re
import subprocess


def violations(name: str, data: bytes) -> list[str]:
    path = PurePosixPath(name.lower())
    reasons = []
    if (path.name in {'secrets.yaml', 'secrets.yml', '.env'}
        or (path.name.startswith('.env.') and path.name != '.env.example')
        or any(part in {'.esphome', '.venv', '.terraform', 'backups', 'local'} for part in path.parts)
        or re.search(r'\.(bin|elf|uf2|gbl|nvm3?|log|tfplan|tfvars|pem|key|p12|pfx|db)$', path.name)
        or re.search(r'\.(tfstate|sqlite)(\.|$)', path.name)
        or path.name.endswith('.tfvars.json')
        or path.name.startswith('credentials.')):
        reasons.append('private/configuration/build artifact')
    if path.suffix in {'.yaml', '.yml'}:
        text = data.decode('utf-8', errors='replace')
        pattern = r'^\s*(?:wifi_ssid|wifi_password|api_encryption_key|ota_password|password|token|api_key|key|ssid)\s*:\s*(.*?)\s*$'
        for match in re.finditer(pattern, text, re.MULTILINE | re.IGNORECASE):
            value = match.group(1).strip().strip('\"\'')
            if not value or value.startswith('#'):
                continue
            if value.startswith(('!secret ', 'REPLACE_WITH_', '${')):
                continue
            reasons.append('literal credential field: use !secret or a documented placeholder')
            break
    return reasons


def main() -> int:
    paths = subprocess.check_output(['git', 'ls-files', '-z']).split(b'\0')
    failed = False
    for raw in filter(None, paths):
        name = raw.decode('utf-8')
        data = subprocess.check_output(['git', 'show', f':{name}'])
        for reason in violations(name, data):
            print(f'BLOCKED {name}: {reason}')
            failed = True
    if not failed:
        print('PASS: staged files contain no forbidden artifacts or literal YAML credentials.')
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
