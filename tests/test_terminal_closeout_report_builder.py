import unittest
from local_terminal_closeout.terminal_closeout_report_builder import generate_report_builder

class TestReportBuilder(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_report_builder())
