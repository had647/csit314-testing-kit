"""
Tests to see if adding keywords to a search of cars will lower or not effect the amount of results
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_test_keywordSearch():
    print("\nRunning keywordSearch Test Oracle now...")

    total = getTotalResultsFound("https://www.gumtree.com.au/s-search.html")
    totalResults = extractTotalIntValue(total)

    searchOne = getTotalResultsFound("https://www.gumtree.com.au/s-car/k0")
    searchOneTotal = extractTotalIntValue(searchOne)

    searchTwo = getTotalResultsFound("https://www.gumtree.com.au/s-car+mitsubishi/k0")
    searchTwoTotal = extractTotalIntValue(searchTwo)

    searchThree = getTotalResultsFound("https://www.gumtree.com.au/s-car+mitsubishi+trailer/k0")
    searchThreeTotal = extractTotalIntValue(searchThree)

    hasFailed = False

    if searchOneTotal > totalResults :
      hasFailed = True

    elif searchTwoTotal > searchOneTotal :
      hasFailed = True

    elif searchThreeTotal > searchTwoTotal :
      hasFailed = True

    # Preparing Variables for output
    testCase = "Results displayed when extra keywords are added to query."

    if hasFailed == False :
        print("\nThe Test Passed!")
        print("The 3rd keyword search total: ",
            searchThreeTotal)
        print("The toal Gumtree listings: ", total)

        totalString = "<=" + str(total)

        outputCSV(testCase, True, totalString, searchThreeTotal)

    else:
        print("\nThe Test Failed!")
        print("The 3rd keyword search total: ",
            searchThreeTotal)
        print("The toal Gumtree listings: ", total)

        totalString = "<=" + str(total)

        outputCSV(testCase, False, totalString, searchThreeTotal)
