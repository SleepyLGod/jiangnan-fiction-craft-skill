# SPDX-License-Identifier: MIT
# Copyright (c) 2026 SleepyLGod and contributors
"""Regression checks for package discovery, licensing, and workflow scope."""
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

    def test_missing_license_text_is_reported(self) -> None:
        files = check_skill.distribution_files(check_skill.ROOT)
        missing = check_skill.ROOT / 'LICENSES' / 'MIT.txt'
        with patch.object(check_skill, 'distribution_files', return_value=[p for p in files if p != missing]):
            with self.assertRaisesRegex(ValueError, 'missing license file: LICENSES/MIT.txt'):
                check_skill.check()

    def test_unlisted_license_directory_file_is_rejected(self) -> None:
        files = check_skill.distribution_files(check_skill.ROOT)
        extra = check_skill.ROOT / 'LICENSES' / 'unlisted-book.txt'
        with patch.object(check_skill, 'distribution_files', return_value=[*files, extra]):
            with self.assertRaisesRegex(ValueError, 'unexpected packaged file: LICENSES/unlisted-book.txt'):
                check_skill.check()

    def test_workflow_is_discovered_and_checked(self) -> None:
        files = check_skill.distribution_files(check_skill.ROOT)
        self.assertIn(check_skill.ROOT / '.github/workflows/check.yml', files)
        self.assertEqual(check_skill.check()['files'], len(files))

    def test_unlisted_workflow_file_is_rejected(self) -> None:
        files = check_skill.distribution_files(check_skill.ROOT)
        extra = check_skill.ROOT / '.github/workflows/unlisted-book.txt'
        with patch.object(check_skill, 'distribution_files', return_value=[*files, extra]):
            with self.assertRaisesRegex(ValueError, 'unexpected packaged file: .github/workflows/unlisted-book.txt'):
                check_skill.check()

    def test_unlisted_issue_template_is_rejected(self) -> None:
        files = check_skill.distribution_files(check_skill.ROOT)
        extra = check_skill.ROOT / '.github/ISSUE_TEMPLATE/unlisted-book.yml'
        with patch.object(check_skill, 'distribution_files', return_value=[*files, extra]):
            with self.assertRaisesRegex(ValueError, 'unexpected packaged file: .github/ISSUE_TEMPLATE/unlisted-book.yml'):
                check_skill.check()


if __name__ == '__main__':
    unittest.main()
