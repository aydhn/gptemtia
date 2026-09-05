import unittest
from local_terminal_closeout.terminal_closeout_gaps import generate_gaps

class TestGaps(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_gaps())
