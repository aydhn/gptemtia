import unittest
from local_terminal_closeout.ultimate_project_ledger_maps import generate_maps

class TestUltimateProjectLedgerMaps(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_maps())
