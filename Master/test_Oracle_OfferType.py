"""
Tests to see if the total results equals the sum of wanted and offering Offer type
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_test_offerType():
    print("\nRunning OfferType Test Oracle now...")

    # large data set by location
    sydney = getTotalResultsFound("https://www.gumtree.com.au/s-sydney/l3003435")
    totalSydney = extractTotalIntValue(sydney)

    sydOffering = getTotalResultsFound("https://www.gumtree.com.au/s-sydney/l3003435?ad=offering")
    sydOfferingTotal = extractTotalIntValue(sydOffering)

    sydWanted = getTotalResultsFound("https://www.gumtree.com.au/s-sydney/l3003435?ad=wanted")
    sydWantedTotal = extractTotalIntValue(sydWanted)

    # small data set by location
    griffith = getTotalResultsFound("https://www.gumtree.com.au/s-griffith-wagga-wagga/l3004629")
    totalGriff = extractTotalIntValue(griffith)

    griffOffering = getTotalResultsFound("https://www.gumtree.com.au/s-griffith-wagga-wagga/l3004629?ad=offering")
    griffOfferingTotal = extractTotalIntValue(griffOffering)

    griffWanted = getTotalResultsFound("https://www.gumtree.com.au/s-griffith-wagga-wagga/l3004629?ad=wanted")
    griffWantedTotal = extractTotalIntValue(griffWanted)

    # Preparing Variables for output
    testCase = "Results Displayed when OfferType of query is altered. Location is set to "

    if calculateTotalTypes(griffOfferingTotal, griffWantedTotal) == totalGriff:
        print("\nThe Test Passed!")
        print("The Sum of Offering + Wanted is: ",
              calculateTotalTypes(griffOfferingTotal, griffWantedTotal))
        print("The total Gumtree provided: ", totalGriff)
        outputCSV(testCase + "Griffith", True, totalGriff, calculateTotalTypes(griffOfferingTotal, griffWantedTotal))
    else:
        print("\nThe Test Failed!")
        print("The Sum of Offering + Wanted is: ",
              calculateTotalTypes(griffOfferingTotal, griffWantedTotal))
        print("The total Gumtree provided: ", totalGriff)
        outputCSV(testCase + "Griffith", False, totalGriff, calculateTotalTypes(griffOfferingTotal, griffWantedTotal))

    if calculateTotalTypes(sydOfferingTotal, sydWantedTotal) == totalSydney:
        print("\nThe Test Passed!")
        print("The Sum of Offering + Wanted is: ",
              calculateTotalTypes(sydOfferingTotal, sydWantedTotal))
        print("The total Gumtree provided: ", totalSydney)
        outputCSV(testCase + "Sydney", True, totalSydney, calculateTotalTypes(sydOfferingTotal, sydWantedTotal))
    else:
        print("\nThe Test Failed!")
        print("The Sum of Offering + Wanted is: ",
              calculateTotalTypes(sydOfferingTotal, sydWantedTotal))
        print("The total Gumtree provided: ", totalSydney)
        outputCSV(testCase + "Sydney", False, totalSydney, calculateTotalTypes(sydOfferingTotal, sydWantedTotal))
