"""
This python file will generate all possible combination of range to test
Gumtree and its ability to return any values within a price range
Get the value directly from Gumtree so the values would be really up-to-date
"""
import requests
from bs4 import BeautifulSoup
import json
hourlyRateRangeMin = []
hourlyRateRangeMax = []
annualSalaryRangeMin = []
annualSalaryRangeMax = []
# --------------------------------------------------------
# Hourly Rate Salary Range
hourlyRateRange = requests.get("https://www.gumtree.com.au/s-jobs/salarytype-hourlyrate/c9302?ad=offering")
hourlyRateRangeSoup = BeautifulSoup(hourlyRateRange.text, 'html.parser')
# Min Hourly Rate Range
minSelect = hourlyRateRangeSoup.find(id="srp-range-filter-min")
minOptions = BeautifulSoup(str(minSelect), 'html.parser')
for option in minOptions.find_all('option'):
    if (option['value'] != ''):
        hourlyRateRangeMin.append(int(option['value']))
# Max Hourly Rate Range
maxSelect = hourlyRateRangeSoup.find(id="srp-range-filter-max")
maxOptions = BeautifulSoup(str(maxSelect), 'html.parser')
for option in maxOptions.find_all('option'):
    if(option['value'] != ''):
        hourlyRateRangeMax.append(int(option['value']))

data = {} # Main JSON Object
data['testdata'] = []
print("Generating data for hourly rate salary type . . .")
for hourlyRateMin in hourlyRateRangeMin:
    for hourlyRateMax in hourlyRateRangeMax:
        if(hourlyRateMin > hourlyRateMax):
            data['testdata'].append({
                'type': 'HourlyRate',
                'url' : 'https://www.gumtree.com.au/s-jobs/salarytype-hourlyrate/salaryrange-' + str(hourlyRateMin) + '__' + str(hourlyRateMax) + '/c9302?ad=offering',
                'expectedMinVal': 0,
                'min': hourlyRateMin,
                'max': hourlyRateMax
            })
        else:
            data['testdata'].append({
                'type': 'HourlyRate',
                'url': 'https://www.gumtree.com.au/s-jobs/salarytype-hourlyrate/salaryrange-' + str(hourlyRateMin) + '__' + str(hourlyRateMax) + '/c9302?ad=offering',
                'expectedMinVal': 1,
                'min': hourlyRateMin,
                'max': hourlyRateMax
            })
print("Finished generating data for hourly rate salary type!")




# --------------------------------------------------------
# Annual Salary Range
annualRateRange = requests.get("https://www.gumtree.com.au/s-jobs/salarytype-annualsalarypackage/c9302?ad=offering")
annualRateRangeSoup = BeautifulSoup(annualRateRange.text, 'html.parser')
# Min Annual Rate Range
minSelect = annualRateRangeSoup.find(id="srp-range-filter-min")
minOptions = BeautifulSoup(str(minSelect), 'html.parser')
for option in minOptions.find_all('option'):
    if (option['value'] != ''):
        annualSalaryRangeMin.append(int(option['value']))
# Max Annual Rate Range
maxSelect = annualRateRangeSoup.find(id="srp-range-filter-max")
maxOptions = BeautifulSoup(str(maxSelect), 'html.parser')
for option in maxOptions.find_all('option'):
    if(option['value'] != ''):
        annualSalaryRangeMax.append(int(option['value']))

print("Generating data for Annual Salary Package type . . .")
for annualSalaryMin in annualSalaryRangeMin:
    for annualSalaryMax in annualSalaryRangeMax:
        if(annualSalaryMin > annualSalaryMax):
            data['testdata'].append({
                'type': 'AnnualSalaryPackage',
                'url' : 'https://www.gumtree.com.au/s-jobs/salarytype-annualsalarypackage/salaryrange-' + str(annualSalaryMin) + '__' + str(annualSalaryMax) + '/c9302?ad=offering',
                'expectedMinVal': 0,
                'min': annualSalaryMin,
                'max': annualSalaryMax
            })
        else:
            data['testdata'].append({
                'type': 'AnnualSalaryPackage',
                'url' : 'https://www.gumtree.com.au/s-jobs/salarytype-annualsalarypackage/salaryrange-' + str(annualSalaryMin) + '__' + str(annualSalaryMax) + '/c9302?ad=offering',
                'expectedMinVal': 1,
                'min': annualSalaryMin,
                'max': annualSalaryMax
            })
print("Finished generating data for Annual Salary Package type!")

print("Generating data for Annual Salary Commission type . . .")
for annualSalaryMin in annualSalaryRangeMin:
    for annualSalaryMax in annualSalaryRangeMax:
        if(annualSalaryMin > annualSalaryMax):
            data['testdata'].append({
                'type': 'AnnualSalaryCommission',
                'url' : 'https://www.gumtree.com.au/s-jobs/salarytype-annualsalarycommission/salaryrange-' + str(annualSalaryMin) + '__' + str(annualSalaryMax) + '/c9302?ad=offering',
                'expectedMinVal': 0,
                'min': annualSalaryMin,
                'max': annualSalaryMax
            })
        else:
            data['testdata'].append({
                'type': 'AnnualSalaryCommission',
                'url' : 'https://www.gumtree.com.au/s-jobs/salarytype-annualsalarycommission/salaryrange-' + str(annualSalaryMin) + '__' + str(annualSalaryMax) + '/c9302?ad=offering',
                'expectedMinVal': 1,
                'min': annualSalaryMin,
                'max': annualSalaryMax
            })
print("Finished generating data for Annual Salary Commission type!")



filename = "Test_Job_Salary_Range_Oracle_URL.txt"
with open(filename, 'w') as outfile:
    json.dump(data, outfile)
print("File containing test data named: " + filename + " is created in the same folder!")