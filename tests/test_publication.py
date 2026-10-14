"""Exercise the publication policy without committing or printing fake secrets."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('publication', Path(__file__).resolve().parents[1] / 'scripts/check_publication.py')
publication = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publication)


class PublicationTest(unittest.TestCase):
    def test_private_artifacts_are_blocked_even_when_forced_into_git(self):
        for name in ['firmware/secrets.yaml', 'nested/secrets.yml', '.env.production',
                     'firmware.bin', 'backup.nvm', 'terraform.tfstate.backup',
                     'prod.tfvars.json', '.terraform/config.json', 'credentials.json']:
            with self.subTest(name=name):
                self.assertTrue(publication.violations(name, b''))

    def test_literal_yaml_credentials_are_blocked(self):
        for field in ['password', 'wifi_password', 'ssid', 'api_encryption_key', 'key']:
            with self.subTest(field=field):
                data = (field + ': "' + 'not-' + 'a-real-credential' + '"\n').encode()
                self.assertTrue(publication.violations('firmware/board.yaml', data))

    def test_secret_references_and_placeholders_are_allowed(self):
        for value in ['!secret wifi_password', 'REPLACE_WITH_YOUR_PASSWORD', '${shared_value}']:
            self.assertFalse(publication.violations('firmware/board.yaml', ('password: ' + value).encode()))
        self.assertFalse(publication.violations('firmware/secrets.example.yaml', b'wifi_ssid: REPLACE_WITH_YOUR_SSID'))


if __name__ == '__main__':
    unittest.main()
