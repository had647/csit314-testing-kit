import unittest
from unittest import TestCase
import requests

class Test(TestCase):
    def test_get_total_results_found(self):

        response = requests.get("https://www.gumtree.com.au/s-search.html")
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()