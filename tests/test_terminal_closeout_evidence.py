import unittest
from local_terminal_closeout.terminal_closeout_evidence import generate_evidence

class TestEvidence(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_evidence())
