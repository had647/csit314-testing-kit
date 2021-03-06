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

    def test_calculateTotalPriceTypes(self):
        fixed = 101
        negotiable = 305
        free = 617
        swapTrade = 2229
        driveAway = 99
        total = fixed + negotiable + free + swapTrade + driveAway
        self.assertEqual(total, 3351)


if __name__ == '__main__':
    unittest.main()
