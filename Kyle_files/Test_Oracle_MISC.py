"""
This oracle will compare the total of test result equals the original result
"""
from Kyle_files.MiscGoodsTest import *

def misc_search_test():

        keyword = "miscellaneous-goods"
        url = "https://www.gumtree.com.au/s-" + keyword + "/c18319"

        total = getTotalResultsFound(url)
        totalResults = extractTotalIntValue(total)

        # ------ OFFERING of MISCELLANEOUS  ------- #

        offering = getTotalResultsFound(url+"?ad=offering")
        wanted = getTotalResultsFound(url+"?ad=wanted")

        if calculateTotalOFFER(offering, wanted) == total :
            print("\nOFFERING in MISCELLANEOUS TEST")
            print("The Test Passed!")
            print("The Sum of each price type: ",
                  calculateTotalOFFER(offering, wanted))
            print("The total Gumtree provided: ", total)

        else:
            print("\nSub Categories in MISCELLANEOUS TEST")
            print("The Test Failed!")
            print("The Sum of each price type: ",
                  calculateTotalOFFER(offering, wanted))
            print("The total Gumtree provided: ", total)

        # ------ END OF OFFERING OF MISCELLANEOUS ------ #

        # ------ Advertisement in REAL ESTATE ------ #

        # ------ END OF ORACLE ADVERTISEMENT TEST

        # ------ END of Advertisement in REAL ESTATE -----