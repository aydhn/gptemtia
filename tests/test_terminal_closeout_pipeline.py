import unittest
from local_terminal_closeout.terminal_closeout_pipeline import generate_pipeline

class TestPipeline(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_pipeline())
