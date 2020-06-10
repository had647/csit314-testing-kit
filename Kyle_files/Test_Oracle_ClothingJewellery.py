"""
This oracle will compare the total of test result equals the original result
"""
from Kyle_files.ClothingAndJewelleryTest import *
from Kyle_files.outputCSV import *

def clothing_jewellery_search_test():

        keyword = "clothing-jewellery"
        url = "https://www.gumtree.com.au/s-" + keyword + "/c18308"

        total = getTotalResultsFound(url)
        totalResults = extractTotalIntValue(total)

        # ------ Categories of Clothing & Jewellery  ------- #

        women = getTotalResultsFound("https://www.gumtree.com.au/s-women-s-clothing/c18570")
        jewellery = getTotalResultsFound("https://www.gumtree.com.au/s-jewellery/c18601")
        womenShoes = getTotalResultsFound("https://www.gumtree.com.au/s-women-s-shoes/c18572")
        men = getTotalResultsFound("https://www.gumtree.com.au/s-men-s-clothing/c18571")
        bags = getTotalResultsFound("https://www.gumtree.com.au/s-bags/c18574")
        menShoes = getTotalResultsFound("https://www.gumtree.com.au/s-men-s-shoes/c18573")
        dressMaking = getTotalResultsFound("https://www.gumtree.com.au/s-dress-making-alterations/c30013")



        testCase = "Results displayed in Miscellaneous Goods in Australia and comparation between its offering plus wanted and the total in Australia"

        totalCategories = calculateTotalCategories(women, jewellery, womenShoes, men, bags, menShoes, dressMaking)
        if  totalCategories == total :
            print("\nOFFERING in MISCELLANEOUS TEST")
            print("The Test Passed!")
            print("The Sum of each price type: ",
                  totalCategories)
            print("The total Gumtree provided: ", total)
            outputCSV(testCase, True, totalResults, totalCategories)

        else:
            print("\nSub Categories in MISCELLANEOUS TEST")
            print("The Test Failed!")
            print("The Sum of each price type: ",
                  totalCategories)
            print("The total Gumtree provided: ", total)
            outputCSV(testCase, True, totalResults, totalCategories)

        # ------ END OF Categories OF Clothing & Jewellery ------ #

        # ------ Advertisement in REAL ESTATE ------ #

        # ------ END OF ORACLE ADVERTISEMENT TEST

        # ------ END of Advertisement in REAL ESTATE -----