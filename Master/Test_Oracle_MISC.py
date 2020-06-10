"""
This oracle will compare the total of test result equals the original result
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *

def misc_search_test():
        print("\nRunning Miscellaneous Goods Test Oracle now...")
        keyword = "miscellaneous-goods"
        url = "https://www.gumtree.com.au/s-" + keyword + "/c18319"

        total = getTotalResultsFound(url)
        totalResults = extractTotalIntValue(total)

        # ------ OFFERING of MISCELLANEOUS  ------- #

        testCase = "Results displayed in Miscellaneous Goods in Australia and comparation between its offering plus wanted and the total in Australia"

        offering = getTotalResultsFound(url+"?ad=offering")
        offeringResult = extractTotalIntValue(offering)
        wanted = getTotalResultsFound(url+"?ad=wanted")
        wantedResult = extractTotalIntValue(wanted)

        totalOffer = calculateTotalOFFER(offeringResult, wantedResult)
        if  totalOffer == total :
            print("\nOFFERING in MISCELLANEOUS TEST")
            print("The Test Passed!")
            print("The Sum of each price type: ",
                  totalOffer)
            print("The total Gumtree provided: ", totalResults)
            outputCSV(testCase, True, totalResults, totalOffer)

        else:
            print("\nSub Categories in MISCELLANEOUS TEST")
            print("The Test Failed!")
            print("The Sum of each price type: ",
                  totalOffer)
            print("The total Gumtree provided: ", totalResults)
            outputCSV(testCase, False, totalResults, totalOffer)

        # ------ END OF OFFERING OF MISCELLANEOUS ------ #