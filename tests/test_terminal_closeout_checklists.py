import unittest
from local_terminal_closeout.terminal_closeout_checklists import generate_checklists

class TestChecklists(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_checklists())
