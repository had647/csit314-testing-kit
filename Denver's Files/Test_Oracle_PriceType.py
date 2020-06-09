from Denver_files.testingResultsFoundByPriceType import *
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


if calculateTotal(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway) == total :
    print("\nThe Test Passed!")
    print("The Sum of each price type: ",
          calculateTotal(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
    print("The total Gumtree provided: ", total)

else:
    print("\nThe Test Failed!")
    print("The Sum of each price type: ",
          calculateTotal(totalFixed, totalNegotiable, totalFree, totalSwapTrade, totalDriveAway))
    print("The total Gumtree provided: ", total)

