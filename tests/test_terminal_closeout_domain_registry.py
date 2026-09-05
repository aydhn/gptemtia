import unittest
from local_terminal_closeout.closeout_domain_registry import create_domain_registry

class TestCloseoutDomainRegistry(unittest.TestCase):
    def test_reg(self):
        self.assertIsNotNone(create_domain_registry())
