"""Unit tests for h5rdmtoolbox.config"""
import unittest

import zenodo_search as zsearch


class TestZenodoSearch(unittest.TestCase):

    def test_search_doi(self):
        self.assertEqual(len(zsearch.search('10.5281/zenodo.8220739')), 1)
        self.assertEqual(len(zsearch.search('doi:10.5281/zenodo.8220739')), 1)
        self.assertEqual(len(zsearch.search('doi:10.5281/zenodo.8220739')), 1)
        self.assertIsInstance(zsearch.search('doi:10.5281/zenodo.8220739'), zsearch.ZenodoRecords)
        self.assertIsInstance(zsearch.search_doi('10.5281/zenodo.8220739'), zsearch.ZenodoRecord)
