import unittest
from local_terminal_closeout.terminal_master_closeout import generate_master_closeout

class TestMasterCloseout(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_master_closeout())
