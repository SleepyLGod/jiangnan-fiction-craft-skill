"""Regression checks for Git metadata exclusion and new-document discovery."""
from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
import unittest
from unittest.mock import patch

import check_skill


class PackageDiscoveryTests(unittest.TestCase):
    """Keep repository metadata out without hiding new skill documents."""

    def test_git_metadata_directory_is_excluded(self) -> None:
        files = check_skill.distribution_files(check_skill.ROOT)
        self.assertFalse(any('.git' in path.relative_to(check_skill.ROOT).parts for path in files))

    def test_git_metadata_file_keeps_full_check_unchanged(self) -> None:
        expected = check_skill.check()
        real_walk = check_skill.os.walk

        def walk_with_git_file(root: Path) -> Iterator[tuple[str, list[str], list[str]]]:
            for directory, subdirs, names in real_walk(root):
                if Path(directory) == check_skill.ROOT:
                    subdirs[:] = [name for name in subdirs if name != '.git']
                    names = [*names, '.git']
                yield directory, subdirs, names

        with patch.object(check_skill.os, 'walk', walk_with_git_file):
            self.assertFalse(check_skill.ROOT / '.git' in check_skill.distribution_files(check_skill.ROOT))
            self.assertEqual(check_skill.check(), expected)

    def test_untracked_document_is_still_discovered(self) -> None:
        real_walk = check_skill.os.walk
        new_name = 'new-analysis-regression.md'

        def walk_with_new_document(root: Path) -> Iterator[tuple[str, list[str], list[str]]]:
            for directory, subdirs, names in real_walk(root):
                if Path(directory) == check_skill.ROOT / 'chapters':
                    names = [*names, new_name]
                yield directory, subdirs, names

        with patch.object(check_skill.os, 'walk', walk_with_new_document):
            self.assertIn(check_skill.ROOT / 'chapters' / new_name, check_skill.distribution_files(check_skill.ROOT))


if __name__ == '__main__':
    unittest.main()
