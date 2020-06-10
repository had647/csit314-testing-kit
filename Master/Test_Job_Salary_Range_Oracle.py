"""
This file is responsible for testing the 3 salary types with range
and ensure the correct number of values is returned.

data file is generated if not exists!
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *
from Master.Salary_Range_Test_Data_Generator import *
import os.path
import json

def run_test_salary_range():
    print("Running Test To Check Salary Range Oracle . . .")
    print("Retrieving list of URLs from the text file . . .\n\n")
    if(not(os.path.exists("Test_Job_Salary_Range_Oracle_URL.txt"))):
        print("Cannot retrieve data file: Test_Job_Salary_Range_Oracle_URL.txt . . .\n\n")
        print("Creating data file Test_Job_Salary_Range_Oracle_URL.txt . . .")
        generateHourlyRateData();
        generateAnnualSalaryData();
        extractSalaryRangeDataFile();

    file = open("Test_Job_Salary_Range_Oracle_URL.txt", "r")
    urlList = file.read()
    urlListObject = json.loads(urlList)

    print("Test for all salary range is running. . .")
    testStillTrue = True
    for urlObject in urlListObject['testdata']:
        salaryType = getTotalResultsFound(urlObject['url'])
        salaryTypeJobsCount = extractTotalIntValue(salaryType)
        if(urlObject['expectedMinVal'] == 1):
            if(salaryTypeJobsCount >= urlObject['expectedMinVal']):
                print("Finished testing salary type '" + urlObject['type'] + "' with range from " + str(urlObject['min']) + " to " + str(urlObject['max']) + "!")
                outputCSV("Results retrieving jobs from salary type '" + urlObject['type'] + "' with range from " + str(urlObject['min']) + " to " + str(urlObject['max']), True, urlObject['expectedMinVal'], salaryTypeJobsCount)
            else:
                if(testStillTrue):
                    testStillTrue = False
                print("Finished testing salary type '" + urlObject['type'] + "' with range from " + str(urlObject['min']) + " to " + str(urlObject['max']) + "!")
                outputCSV("Results retrieving jobs from salary type '" + urlObject['type'] + "' with range from " + str(urlObject['min']) + " to " + str(urlObject['max']), False, urlObject['expectedMinVal'],
                          salaryTypeJobsCount)
        elif(urlObject['expectedMinVal'] == 0):
            if (salaryTypeJobsCount == urlObject['expectedMinVal']):
                print("Finished testing salary type '" + urlObject['type'] + "' with range from " + str(
                    urlObject['min']) + " to " + str(urlObject['max']) + "!")
                outputCSV("Results retrieving jobs from salary type '" + urlObject['type'] + "' with range from " + str(
                    urlObject['min']) + " to " + str(urlObject['max']), True, urlObject['expectedMinVal'],
                          salaryTypeJobsCount)
            else:
                if (testStillTrue):
                    testStillTrue = False
                print("Finished testing salary type '" + urlObject['type'] + "' with range from " + str(
                    urlObject['min']) + " to " + str(urlObject['max']) + "!")
                outputCSV("Results retrieving jobs from salary type '" + urlObject['type'] + "' with range from " + str(
                    urlObject['min']) + " to " + str(urlObject['max']), False, urlObject['expectedMinVal'],
                          salaryTypeJobsCount)
    print("Test for all salary range is finished !")
    # 1 false -> the test is not success
    outputCSV("Results testing all salary ranges for Hourly Rate, Annual Salary (Package and Commission) in Gumtree", testStillTrue, 0, 1)
    print("Finished Testing To Check Salary Range Oracle !")