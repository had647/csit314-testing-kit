from Denver_files.testingResultsFoundByOfferingType import

premium = getTotalResultsFound("https://www.gumtree.com.au/s-ads?premiumAds=y")
totalPremium = extractTotalIntValue(premium)

offering = getTotalResultsFound("https://www.gumtree.com.au/s-ads?ad=offering&premiumAds=y")
totalOffering = extractTotalIntValue(offering)

wanted = getTotalResultsFound("https://www.gumtree.com.au/s-ads?ad=wanted&premiumAds=y")
totalWanted = extractTotalIntValue(wanted)


if calculateTotal(totalOffering, totalWanted) == totalPremium :
    print("\nThe Test Passed!")
    print("The Sum of all premium offer types: ",
          calculateTotal(totalOffering, totalWanted))
    print("The total Gumtree provided: ", totalPremium)

else:
    print("\nThe Test Failed!")
    print("The Sum of all premium offer types: ",
          calculateTotal(totalOffering, totalWanted))
    print("The total Gumtree provided: ", totalPremium)

