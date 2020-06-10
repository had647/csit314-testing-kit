"""
Tests to see if the total results of premium ads equals the sum of both offering and wanted ads
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_test_premiumOfferType():
    print("\nRunning PriceType Test Oracle now...")

    premium = getTotalResultsFound("https://www.gumtree.com.au/s-ads?premiumAds=y")
    totalPremium = extractTotalIntValue(premium)

    offering = getTotalResultsFound("https://www.gumtree.com.au/s-ads?ad=offering&premiumAds=y")
    totalOffering = extractTotalIntValue(offering)

    wanted = getTotalResultsFound("https://www.gumtree.com.au/s-ads?ad=wanted&premiumAds=y")
    totalWanted = extractTotalIntValue(wanted)

    # Preparing Variables for output
    testCase = "Results displayed when offer type is altered."

    if calculateTotalOFFER(totalOffering, totalWanted) == totalPremium :
    print("\nThe Test Passed!")
    print("The Sum of all premium offer types: ",
          calculateTotalOFFER(totalOffering, totalWanted))
    print("The total Gumtree provided: ", totalPremium)
    outputCSV(testCase, True, totalPremium, calculateTotalOFFER(totalOffering, totalWanted))

    else :
    print("\nThe Test Failed!")
    print("The Sum of all premium offer types: ",
          calculateTotalOFFER(totalOffering, totalWanted))
    print("The total premium ads Gumtree provided: ", totalPremium)
    outputCSV(testCase, False, totalPremium, calculateTotalOFFER(totalOffering, totalWanted))
