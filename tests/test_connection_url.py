import base64
import importlib.util
import contextlib
import io
from pathlib import Path
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

spec = importlib.util.spec_from_file_location('connection_url', Path(__file__).resolve().parents[1] / 'scripts/connection_url.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ConnectionURLTest(unittest.TestCase):
    def test_special_base64_survives_query_parsing(self):
        key = base64.b64encode(bytes([251, 255]) * 16).decode()
        url = module.connection_url('zac93-wroom.local', key)
        self.assertIn('%2B', url)
        self.assertIn('%2F', url)
        self.assertIn('%3D', url)
        self.assertEqual(parse_qs(urlparse(url).query)['key'], [key])

    def test_ipv6(self):
        url = module.connection_url('2001:db8::1', base64.b64encode(bytes(32)).decode())
        self.assertEqual(urlparse(url).hostname, '2001:db8::1')

    def test_cli_displays_only_the_explicitly_requested_private_url(self):
        key = base64.b64encode(bytes(range(32))).decode()
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(module.getpass, 'getpass', return_value=key), \
                patch('sys.argv', ['connection_url.py', 'example.invalid']), \
                contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            module.main()
        lines = stdout.getvalue().splitlines()
        self.assertEqual(len(lines), 2)
        self.assertIn('Private connection URL', lines[0])
        self.assertEqual(lines[1], module.connection_url('example.invalid', key))
        self.assertEqual(stderr.getvalue(), '')

    def test_reject_bad_key_host_and_port(self):
        valid = base64.b64encode(bytes(32)).decode()
        for host, key, port in [('host', 'bad', 6053), ('host', base64.b64encode(b'x').decode(), 6053), ('host/path', valid, 6053), ('host', valid, 0)]:
            with self.subTest(host=host, port=port), self.assertRaises(ValueError):
                module.connection_url(host, key, port)


if __name__ == '__main__':
    unittest.main()
