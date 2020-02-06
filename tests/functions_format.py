#!/usr/bin/env python3

"""
Test for required internal structure of Python files
"""

import unittest
import os


def is_python_file(path):
    """Return True if path is a Python file"""
    return os.path.isfile(path) and path.endswith(".py")


class TestContentOfFiles(unittest.TestCase):
    """Test to go through files and check internal structure"""

    path = "activities/"

    def test_files_have_expected_content(self):
        """Check that files contain required pieces"""
        for filename in os.listdir(self.path):
            full_path = os.path.join(self.path, filename)
            if not is_python_file(full_path):
                continue
            with open(full_path) as file_handle:
                content = file_handle.read()
                self.assertRegex(
                    content,
                    r"\nif __name__ == .__main__.:",
                    msg=(
                        "File {full_path} does not contain"
                        " the 'if __name__...' part".format(**locals())
                    ),
                )
                self.assertRegex(
                    content,
                    r"\ndef run_.+\(",
                    msg=(
                        "File {full_path} does not contain any functions"
                        " with the 'run_' prefix".format(**locals())
                    ),
                )


if __name__ == "__main__":
    unittest.main()
