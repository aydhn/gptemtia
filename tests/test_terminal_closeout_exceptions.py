import unittest
from local_terminal_closeout.terminal_closeout_exceptions import generate_exceptions

class TestExceptions(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_exceptions())
