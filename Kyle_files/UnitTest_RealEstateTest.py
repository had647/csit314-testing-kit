import unittest
from unittest import TestCase
import requests
from bs4 import BeautifulSoup

class Test(TestCase):
    def test_get_total_results_found(self):

        response = requests.get("https://www.gumtree.com.au/s-search.html")
        self.assertTrue(response)

    def test_calculateTotalAds(self):
        premiumAdsResults = 101
        featureAdsResults = 305
        topAdsResults = 617
        highlightAdsResults = 2229
        urgentAdsResults = 99
        priceDropAdsResults = 26
        totalAds = premiumAdsResults + featureAdsResults + topAdsResults + highlightAdsResults + urgentAdsResults + priceDropAdsResults
        self.assertEqual(totalAds, 3377)

    def test_calculateTotalSubRE(self):
        flatshare = 6412
        rent = 5518
        saleBusiness = 2104
        saleProperty = 1664
        office = 818
        parking = 305
        roomshare = 446
        land = 1005
        reService = 0
        other = 390 
        shortTerm = 225
        totalSubRE = flatshare + rent + saleBusiness + saleProperty + office + parking + roomshare + land + reService + other + shortTerm
        self.assertEqual(totalSubRE, 18887)

if __name__ == '__main__':
    unittest.main()