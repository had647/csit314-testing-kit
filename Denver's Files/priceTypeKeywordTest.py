from Denver_files.testingResultsFoundByPriceType import *

import random

keywordList = ["car", "boat", "television"]

keyword = keywordList[random.randint(0, 2)]

#print(keyword)

url = "https://www.gumtree.com.au/s-" + keyword + "/k0"

totalResults = getTotalResultsFound(url)
total = extractTotalIntValue(totalResults)

fixed = getTotalResultsFound(url + "?price-type=fixed")
totalFixed = extractTotalIntValue(fixed)

negotiable = getTotalResultsFound(url + "?price-type=negotiable")
totalNegotiable = extractTotalIntValue(negotiable)

free = getTotalResultsFound(url + "?price-type=free")
totalFree = extractTotalIntValue(free)

swapTrade = getTotalResultsFound(url + "?price-type=swap-trade")
totalSwapTrade = extractTotalIntValue(swapTrade)

driveAway = getTotalResultsFound(url + "?price-type=driveaway")
totalDriveAway = extractTotalIntValue(driveAway)


if calculateTotal(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway) == total :
    print("\nThe Test Passed!")
    print("The Sum of each price type, ",
          calculateTotal(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
    print("The total Gumtree provided: ", total)

else:
    print("\nThe Test Failed!")
    print("The Sum of each price type: ",
          calculateTotal(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
    print("The total Gumtree provided: ", total)

