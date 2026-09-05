import unittest
from local_terminal_closeout.final_archive_catalog import generate_archive_catalog

class TestFinalArchiveCatalog(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_archive_catalog())
