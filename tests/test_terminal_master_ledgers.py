import unittest
from local_terminal_closeout.terminal_master_ledgers import generate_ledgers

class TestMasterLedgers(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_ledgers())
