"""Keep verified firmware and CI dependency closures consistent."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def pins(name):
    return dict(re.findall(r"^([A-Za-z0-9_.-]+)==([^ ;\\\n]+)",
                           (ROOT / name).read_text(), re.MULTILINE))


def marked_pins(text):
    result = {}
    for line in text.splitlines():
        match = re.fullmatch(r"([A-Za-z0-9_.-]+)==([^ ;]+)(?: *; *(.*))?",
                             line.rstrip(" \\") )
        if not match:
            continue
        name, version, marker = match.groups()
        key = (name.lower().replace("_", "-"), marker or "")
        if key in result:
            raise ValueError(f"Duplicate dependency marker: {key}")
        result[key] = version
    return result


class DependencyLockTests(unittest.TestCase):
    def test_direct_versions_are_current(self):
        for source, lock in [("requirements.txt", "requirements.lock"),
                             ("requirements-ci.in", "requirements-ci.lock"),
                             ("requirements-build.in", "requirements-build.lock")]:
            direct, locked = pins(source), pins(lock)
            self.assertTrue(direct)
            self.assertEqual(direct, {name: locked.get(name) for name in direct})

    def test_ci_preserves_firmware_dependencies(self):
        firmware = marked_pins((ROOT / "requirements.lock").read_text())
        ci = marked_pins((ROOT / "requirements-ci.lock").read_text())
        self.assertEqual(firmware, {key: ci.get(key) for key in firmware})

    def test_every_dependency_has_artifact_hashes(self):
        for name in ["requirements.lock", "requirements-ci.lock", "requirements-build.lock"]:
            entries = re.split(r"(?m)(?=^[A-Za-z0-9_.-]+==)", (ROOT / name).read_text())[1:]
            self.assertTrue(entries)
            self.assertTrue(all("--hash=sha256:" in entry for entry in entries))

    def test_marker_comparison_keeps_every_platform_variant(self):
        original = 'package==1 ; sys_platform == "darwin"\npackage==2 ; sys_platform == "linux"\n'
        changed = original.replace('package==1', 'package==3')
        self.assertNotEqual(marked_pins(original), marked_pins(changed))
        self.assertEqual(len(marked_pins(original)), 2)
