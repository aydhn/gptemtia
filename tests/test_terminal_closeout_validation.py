import unittest
from local_terminal_closeout.terminal_closeout_validation import generate_validation

class TestValidation(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_validation())
