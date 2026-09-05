import unittest
from local_terminal_closeout.closeout_config import list_local_terminal_closeout_profiles

class TestCloseoutConfig(unittest.TestCase):
    def test_list(self):
        self.assertTrue(len(list_local_terminal_closeout_profiles()) > 0)
