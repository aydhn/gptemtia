import unittest
from local_terminal_closeout.handover_constitution_maps import generate_handover_maps

class TestHandoverConstitutionMaps(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_handover_maps())
