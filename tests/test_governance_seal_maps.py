import unittest
from local_terminal_closeout.governance_seal_maps import generate_seal_maps

class TestGovernanceSealMaps(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_seal_maps())
