import unittest
from local_terminal_closeout.terminal_closeout_issues import generate_issues

class TestIssues(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_issues())
