import unittest
from local_terminal_closeout.handover_constitution import generate_handover_constitution

class TestHandoverConstitution(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_handover_constitution())
