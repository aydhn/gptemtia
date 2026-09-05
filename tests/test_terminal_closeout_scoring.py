import unittest
from local_terminal_closeout.terminal_closeout_scoring import generate_scoring

class TestScoring(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_scoring())
