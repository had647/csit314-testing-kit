import unittest
import requests
from bs4 import BeautifulSoup

class MyTestCase(unittest.TestCase):
    def test_getTotalResultsFound(self):
        response = requests.get("https://www.gumtree.com.au/s-search.html")
        # Testing that we can get a response from GumTree
        self.assertTrue(response)


        soup = BeautifulSoup(response.text, 'html.parser')
        results_list = soup.find(class_='breadcrumbs__summary--enhanced')
        result = results_list.get_text()
        # Testing that we get the correct element that returns the Results
        self.assertRegex(str(result), "Results")

    def test_extractTotalIntValue(self):
        result = "2788336 Results:  in Australia"
        total = int(result.split()[0])
        # Testing that the total is only the Int value from the string
        self.assertEqual(total, 2788336)

    def test_calculateTotal(self):
        act = 200
        nsw = 654
        nt = 544
        qld = 5435
        sa = 456
        tas = 545
        vic = 734
        wa = 74
        # total = 8642

        totalFromAllStates = act + nsw + nt + qld + sa + tas + vic + wa
        # Testing that the sum matches the total
        self.assertEqual(totalFromAllStates, 8642)

    def test_calculateTotal(self):
        offering = 501
        wanted = 113
        # total = 614

        totalFromOfferType = offering + wanted
        # Testing that the sum matches the total
        self.assertEqual(totalFromOfferType, 614)


if __name__ == '__main__':
    unittest.main()
