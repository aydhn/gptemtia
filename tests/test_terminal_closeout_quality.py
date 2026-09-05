import unittest
from local_terminal_closeout.terminal_closeout_quality import generate_quality

class TestQuality(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_quality())
