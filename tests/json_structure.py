#!/usr/bin/env python3

"""
Test for JSON fomat in activities
"""

import unittest
import os
import json


def is_json_file(path):
    """Return True if path is a JSON file"""
    return os.path.isfile(path) and path.endswith(".json")


class TestContentOfJsonFiles(unittest.TestCase):
    """Test to go through files and check internal structure and content"""

    path = "activities/"

    def test_files_have_expected_content(self):
        """Check that files contain required pieces"""
        for filename in os.listdir(self.path):
            full_path = os.path.join(self.path, filename)
            if not is_json_file(full_path):
                continue

            with open(full_path) as file_handle:
                try:
                    content = json.load(file_handle)
                except json.JSONDecodeError as err:  # noqa: F841
                    self.fail(
                        "File {full_path} is not properly formatted JSON: {err}".format(
                            **locals()
                        )
                    )
                self.assertIn(
                    "tasks",
                    content,
                    msg=("tasks key not in {full_path} file".format(**locals())),
                )
                tasks = content["tasks"]
                self.assertIsInstance(
                    tasks,
                    list,
                    msg="tasks must be a list (of tasks), not {provided_type}".format(
                        provided_type=type(tasks)
                    ),
                )
                self.assertTrue(tasks, msg="tasks list must contain at least one item")
                for task in tasks:
                    self.assertIsInstance(
                        task,
                        dict,
                        msg="task must be a dictionary, not {provided_type}".format(
                            provided_type=type(tasks)
                        ),
                    )
                    self.assertTrue(task, msg="task must be a non-empty dictionary")


if __name__ == "__main__":
    unittest.main()
