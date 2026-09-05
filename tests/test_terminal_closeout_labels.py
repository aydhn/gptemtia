import unittest
from local_terminal_closeout.closeout_labels import list_terminal_closeout_domain_labels

class TestCloseoutLabels(unittest.TestCase):
    def test_list(self):
        self.assertTrue(len(list_terminal_closeout_domain_labels()) > 0)
