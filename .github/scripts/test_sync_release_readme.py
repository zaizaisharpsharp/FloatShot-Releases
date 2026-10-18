"""Offline regression coverage for README release synchronization."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sync_release_readme as sync


class ReadmeTests(unittest.TestCase):
    def setUp(self):
        self.release = {
            "tag_name": "v0.14.1", "draft": False, "prerelease": False,
            "body": "# FloatShot v0.14.1\n\nA public release.\n\n- Fixed tray gestures.\n\nBuilt and tested on Windows; updater ZIP SHA-256 verified.",
            "assets": [{"name": x} for x in sync.REQUIRED],
        }

    def test_render_links_and_notes(self):
        block = sync.render(self.release, [self.release])
        self.assertIn("v0.14.1/FloatShot-Setup.exe", block)
        self.assertIn("Fixed tray gestures", block)
        self.assertIn("Recent releases", block)
        self.assertEqual(block.count(sync.START), 1)
        self.assertEqual(block.count(sync.END), 1)

    def test_exactly_one_marked_block(self):
        old = "Header\n" + sync.START + "\nold\n" + sync.END + "\nFooter\n"
        result = sync.replace_block(old, sync.render(self.release, [self.release]))
        self.assertTrue(result.startswith("Header\n"))
        self.assertTrue(result.endswith("\nFooter\n"))
        self.assertNotIn("\nold\n", result)
        with self.assertRaises(ValueError):
            sync.replace_block("Header only", "replacement")

    def test_reject_unverified_or_prerelease(self):
        bad = dict(self.release, assets=[])
        with self.assertRaises(ValueError):
            sync.render(bad, [bad])
        bad = dict(self.release, prerelease=True)
        with self.assertRaises(ValueError):
            sync.render(bad, [bad])

    def test_recent_versions_and_deduplication(self):
        other = dict(self.release, tag_name="v0.14.0")
        block = sync.render(self.release, [self.release, self.release, other])
        self.assertEqual(block.count("- [v0.14.1]"), 1)
        self.assertIn("- [v0.14.0]", block)


if __name__ == "__main__":
    unittest.main()
