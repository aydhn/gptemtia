import unittest
from local_terminal_closeout.final_archive_catalog_maps import generate_archive_catalog_maps

class TestFinalArchiveCatalogMaps(unittest.TestCase):
    def test_gen(self):
        self.assertIsNotNone(generate_archive_catalog_maps())
