import unittest
from local_terminal_closeout.closeout_models import build_terminal_closeout_domain_id

class TestCloseoutModels(unittest.TestCase):
    def test_build(self):
        self.assertEqual(build_terminal_closeout_domain_id("test"), "dom_test")
