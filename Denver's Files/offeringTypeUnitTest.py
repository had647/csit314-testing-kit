import unittest
from unittest import TestCase
import requests
from bs4 import BeautifulSoup

class Test(TestCase):
    def test_getTotalResultsFound(self):

        response = requests.get("https://www.gumtree.com.au/s-search.html")
        self.assertTrue(response)

    def test_extractTotalIntValue(self):
        result = "2788336 Results:  in Australia"
        total = int(result.split()[0])
        # Testing that the total is only the Int value from the string
        self.assertEqual(total, 2788336)

    def test_calculateTotal(self):
        offering = 101
        wanted = 305
        total = offering + wanted
        self.assertEqual(total, 406)


if __name__ == '__main__':
    unittest.main()
