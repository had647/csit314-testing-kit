"""
This file is responsible for testing the job categories and comparing
the sum of jobs in all categories with the total number of jobs
"""
from had647_files.Generic_Test_Lib import *
from had647_files.outputCSV import *
import json

def run_test_job_categories_with_total_job_count():
    print("Running Test To Check Jobs Count For All Categories With Total Jobs Count Oracle . . .")
    print("Retrieving list of URLs from the text file . . .")
    file = open("Test_Job_Categories_With_Total_Jobs_Count_Oracle_URL.txt", "r")
    urlList = file.read()
    urlListObject = json.loads(urlList)

    allJobs = getTotalResultsFound(urlListObject["AllJobs"])
    allJobsCount = extractTotalIntValue(allJobs)

    sumAllJobsInCategories = 0
    for urlObject in urlListObject['Categories']:
        job = getTotalResultsFound(urlObject['url'])
        sumAllJobsInCategories += extractTotalIntValue(job)

    passed = False
    if sumAllJobsInCategories == allJobsCount:
        print("\nThe Test Passed!")
        print("The sum of each category of job: ", sumAllJobsInCategories)
        print("The total number of jobs Gumtree provided: ", allJobsCount)
        passed = True
    else:
        print("\nThe Test Failed!")
        print("The sum of each category of job: ", sumAllJobsInCategories)
        print("The total number of jobs Gumtree provided: ", allJobsCount)

    outputCSV("Results comparing the sum of each category of job with the total number of jobs in Gumtree", passed, allJobsCount, sumAllJobsInCategories)
run_test_job_categories_with_total_job_count()