import unittest
from local_terminal_closeout.terminal_closeout_no_go_safe_go import generate_no_go

class TestNoGo(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_no_go())
