"""
Tests to see if the total results equals the sum of all price types
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_test_priceType():
    print("\nRunning PriceType Test Oracle now...")

    totalResults = getTotalResultsFound("https://www.gumtree.com.au/s-search.html")
    total = extractTotalIntValue(totalResults)

    fixed = getTotalResultsFound("https://www.gumtree.com.au/s-ads?price-type=fixed")
    totalFixed = extractTotalIntValue(fixed)

    negotiable = getTotalResultsFound("https://www.gumtree.com.au/s-ads?price-type=negotiable")
    totalNegotiable = extractTotalIntValue(negotiable)

    free = getTotalResultsFound("https://www.gumtree.com.au/s-ads?price-type=free")
    totalFree = extractTotalIntValue(free)

    swapTrade = getTotalResultsFound("https://www.gumtree.com.au/s-ads?price-type=swap-trade")
    totalSwapTrade = extractTotalIntValue(swapTrade)

    driveAway = getTotalResultsFound("https://www.gumtree.com.au/s-ads?price-type=driveaway")
    totalDriveAway = extractTotalIntValue(driveAway)

    # Preparing Variables for output
    testCase = "Results Displayed when PriceType of query is altered."

    if calculateTotalPriceTypes(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway) == total :
        print("\nThe Test Passed!")
        print("The Sum of each price type: ",
            calculateTotalPriceTypes(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
        print("The total Gumtree provided: ", total)
        outputCSV(testCase, True, total, calculateTotalPriceTypes(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
    else:
        print("\nThe Test Failed!")
        print("The Sum of each price type: ",
            calculateTotalPriceTypes(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
        print("The total Gumtree provided: ", total)
        outputCSV(testCase, False, total, calculateTotalPriceTypes(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
