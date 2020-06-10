import unittest
import requests
from bs4 import BeautifulSoup

class MyTestCase(unittest.TestCase):
    def test_generateHourlyRateData(self):
        hourlyRateRange = requests.get("https://www.gumtree.com.au/s-jobs/salarytype-hourlyrate/c9302?ad=offering")
        # See if we already got a response from Gumtree
        self.assertTrue(hourlyRateRange)


        hourlyRateRangeSoup = BeautifulSoup(hourlyRateRange.text, 'html.parser')
        # Min Hourly Rate Range
        minSelect = hourlyRateRangeSoup.find(id="srp-range-filter-min")
        minOptions = BeautifulSoup(str(minSelect), 'html.parser')
        testMin = []
        for option in minOptions.find_all('option'):
            if (option['value'] != ''):
                testMin.append(int(option['value']))
        self.assertEqual(len(testMin), 11)  # Check if we got all 11 values
        # Max Hourly Rate Range
        maxSelect = hourlyRateRangeSoup.find(id="srp-range-filter-max")
        maxOptions = BeautifulSoup(str(maxSelect), 'html.parser')
        testMax = []
        for option in maxOptions.find_all('option'):
            if (option['value'] != ''):
                testMax.append(int(option['value']))
        self.assertEqual(len(testMax), 11)  # Check if we got all 11 values

    def test_generateAnnualSalaryData(self):
        annualRateRange = requests.get(
            "https://www.gumtree.com.au/s-jobs/salarytype-annualsalarypackage/c9302?ad=offering")
        annualRateRangeSoup = BeautifulSoup(annualRateRange.text, 'html.parser')
        # Min Annual Rate Range
        minSelect = annualRateRangeSoup.find(id="srp-range-filter-min")
        minOptions = BeautifulSoup(str(minSelect), 'html.parser')
        testMin = []
        for option in minOptions.find_all('option'):
            if (option['value'] != ''):
                testMin.append(int(option['value']))
        self.assertEqual(len(testMin), 11)  # Check if we got all 11 values
        # Max Annual Rate Range
        maxSelect = annualRateRangeSoup.find(id="srp-range-filter-max")
        maxOptions = BeautifulSoup(str(maxSelect), 'html.parser')
        testMax = []
        for option in maxOptions.find_all('option'):
            if (option['value'] != ''):
                testMax.append(int(option['value']))
        self.assertEqual(len(testMax), 11)  # Check if we got all 11 values


if __name__ == '__main__':
    unittest.main()
