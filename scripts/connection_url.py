#!/usr/bin/env python3
"""Create an ESPHome Z-Wave JS URL without exposing the key in shell history."""
import argparse
import base64
import binascii
import getpass
import ipaddress
import re
from urllib.parse import quote


def connection_url(host: str, key: str, port: int = 6053) -> str:
    if not 1 <= port <= 65535:
        raise ValueError("Port must be between 1 and 65535")
    try:
        addr = ipaddress.ip_address(host.strip('[]'))
        host = f'[{addr}]' if addr.version == 6 else str(addr)
    except ValueError:
        if not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?', host):
            raise ValueError("Use a hostname or IP address, without a scheme or path") from None
    try:
        raw = base64.b64decode(key, validate=True)
    except (ValueError, binascii.Error):
        raise ValueError("API encryption key must be Base64") from None
    if len(raw) != 32:
        raise ValueError("API encryption key must decode to 32 bytes")
    return f'esphome://{host}:{port}?key={quote(key, safe="")}'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('host')
    parser.add_argument('--port', type=int, default=6053)
    args = parser.parse_args()
    key = getpass.getpass('ESPHome API encryption key (hidden): ').strip()
    try:
        result = connection_url(args.host, key, args.port)
    except ValueError as exc:
        parser.error(str(exc))
    print('Private connection URL — contains your key; do not publish:')
    print(result)


if __name__ == '__main__':
    main()
