"""
This file is responsible for testing the salary types and comparing
the sum of jobs in different salary types with the total number of jobs
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *
import json

def run_test_salary_types_with_total_job_count():
    print("Running Test To Check Jobs Count For All Types With Total Jobs Count Oracle . . .")
    print("Retrieving list of URLs from the text file . . .")
    file = open("Test_Job_Salary_With_Total_Jobs_Count_Oracle_URL.txt", "r")
    urlList = file.read()
    urlListObject = json.loads(urlList)

    allJobs = getTotalResultsFound(urlListObject["AllJobs"])
    allJobsCount = extractTotalIntValue(allJobs)

    sumAllJobsInSalaryTypes = 0
    for urlObject in urlListObject['SalaryTypes']:
        job = getTotalResultsFound(urlObject['url'])
        sumAllJobsInSalaryTypes += extractTotalIntValue(job)

    passed = False
    if sumAllJobsInSalaryTypes == allJobsCount:
        print("\nThe Test Passed!")
        print("The sum of each type of job: ", sumAllJobsInSalaryTypes)
        print("The total number of jobs Gumtree provided: ", allJobsCount)
        passed = True
    else:
        print("\nThe Test Failed!")
        print("The sum of each type of job: ", sumAllJobsInSalaryTypes)
        print("The total number of jobs Gumtree provided: ", allJobsCount)

    outputCSV("Results comparing the sum of each type of salary with the total number of jobs in Gumtree", passed, allJobsCount, sumAllJobsInSalaryTypes)