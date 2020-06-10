"""
Tests to see if the total results equals the sum of wanted and offering Offer type
"""
from Dans_files.collectRequiredResults import *

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

if calculateTotal(griffOfferingTotal, griffWantedTotal) == totalGriff:
    print("\nThe Test Passed!")
    print("The Sum of Offering + Wanted is: ",
          calculateTotal(griffOfferingTotal, griffWantedTotal))
    print("The total Gumtree provided: ", totalGriff)
else:
    print("\nThe Test Failed!")
    print("The Sum of Offering + Wanted is: ",
          calculateTotal(griffOfferingTotal, griffWantedTotal))
    print("The total Gumtree provided: ", totalGriff)

if calculateTotal(sydOfferingTotal, sydWantedTotal) == totalSydney:
    print("\nThe Test Passed!")
    print("The Sum of Offering + Wanted is: ",
          calculateTotal(sydOfferingTotal, sydWantedTotal))
    print("The total Gumtree provided: ", totalSydney)
else:
    print("\nThe Test Failed!")
    print("The Sum of Offering + Wanted is: ",
          calculateTotal(sydOfferingTotal, sydWantedTotal))
    print("The total Gumtree provided: ", totalSydney)

