import unittest
from local_terminal_closeout.ultimate_project_ledger import generate_ultimate_project_ledger

class TestUltimateProjectLedger(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_ultimate_project_ledger())
