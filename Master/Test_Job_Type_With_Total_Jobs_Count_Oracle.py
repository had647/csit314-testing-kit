"""
This file is responsible for testing the job types and comparing
the sum of jobs in all types with the total number of jobs
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *
import json

def run_test_job_types_with_total_job_count():
    print("Running Test To Check Jobs Count For All Types With Total Jobs Count Oracle . . .")
    print("Retrieving list of URLs from the text file . . .")
    file = open("Test_Job_Type_With_Total_Jobs_Count_Oracle_URL.txt", "r")
    urlList = file.read()
    urlListObject = json.loads(urlList)

    allJobs = getTotalResultsFound(urlListObject["AllJobs"])
    allJobsCount = extractTotalIntValue(allJobs)

    sumAllJobsInTypes = 0
    for urlObject in urlListObject['JobTypes']:
        job = getTotalResultsFound(urlObject['url'])
        sumAllJobsInTypes += extractTotalIntValue(job)

    passed = False
    if sumAllJobsInTypes == allJobsCount:
        print("\nThe Test Passed!")
        print("The sum of each type of job: ", sumAllJobsInTypes)
        print("The total number of jobs Gumtree provided: ", allJobsCount)
        passed = True
    else:
        print("\nThe Test Failed!")
        print("The sum of each type of job: ", sumAllJobsInTypes)
        print("The total number of jobs Gumtree provided: ", allJobsCount)

    outputCSV("Results comparing the sum of each type of job with the total number of jobs in Gumtree", passed, allJobsCount, sumAllJobsInTypes)