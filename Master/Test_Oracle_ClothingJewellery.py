"""
This oracle will compare the total of test result equals the original result
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_clothing_jewellery_search_test():
        print("\nRunning Clothing and Jewellery Test Oracle now...")
        keyword = "clothing-jewellery"
        url = "https://www.gumtree.com.au/s-" + keyword + "/c18308"

        total = getTotalResultsFound(url)
        totalResults = extractTotalIntValue(total)

        # ------ Categories of Clothing & Jewellery  ------- #

        women = getTotalResultsFound("https://www.gumtree.com.au/s-women-s-clothing/c18570")
        womenResult = extractTotalIntValue(women)
        jewellery = getTotalResultsFound("https://www.gumtree.com.au/s-jewellery/c18601")
        jewelleryResult = extractTotalIntValue(jewellery)
        womenShoes = getTotalResultsFound("https://www.gumtree.com.au/s-women-s-shoes/c18572")
        womenShoesResult = extractTotalIntValue(womenShoes)
        men = getTotalResultsFound("https://www.gumtree.com.au/s-men-s-clothing/c18571")
        menResult = extractTotalIntValue(men)
        bags = getTotalResultsFound("https://www.gumtree.com.au/s-bags/c18574")
        bagsResult = extractTotalIntValue(bags)
        menShoes = getTotalResultsFound("https://www.gumtree.com.au/s-men-s-shoes/c18573")
        menShoesResult = extractTotalIntValue(menShoes)
        dressMaking = getTotalResultsFound("https://www.gumtree.com.au/s-dress-making-alterations/c30013")
        dressMakingResult = extractTotalIntValue(dressMaking)


        testCase = "Results displayed in Clothing And Jewellery in Australia and its sub categories in Australia"

        totalCategories = calculateTotalCategories(womenResult, jewelleryResult, womenShoesResult, menResult, bagsResult, menShoesResult, dressMakingResult)
        if  totalCategories == totalResults :
            print("\nTest of Sub Categories of Clothing Jewellery")
            print("The Test Passed!")
            print("The Sum of each price type: ",
                  totalCategories)
            print("The total Gumtree provided: ", totalResults)
            outputCSV(testCase, True, totalResults, totalCategories)

        else:
            print("\nTest of Sub Categories of Clothing Jewellery")
            print("The Test Failed!")
            print("The Sum of each price type: ",
                  totalCategories)
            print("The total Gumtree provided: ", totalResults)
            outputCSV(testCase, False, totalResults, totalCategories)

        # ------ END OF Categories OF Clothing & Jewellery ------ #