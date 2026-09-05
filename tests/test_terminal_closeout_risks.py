import unittest
from local_terminal_closeout.terminal_closeout_risks import generate_risks

class TestRisks(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_risks())
