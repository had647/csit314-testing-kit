"""
This oracle will compare the total of test result equals the original result
"""
from Kyle_files.RealEstateTest import *

keyword = "real-estate"
url = "https://www.gumtree.com.au/s-" + keyword + "/c9296"

total = getTotalResultsFound(url)
totalResults = extractTotalIntValue(total)

# ------ TYPE of REAL ESTATE  ------- #

flatShare = getTotalResultsFound("https://www.gumtree.com.au/s-flatshare-houseshare/c18294")

rent = getTotalResultsFound("https://www.gumtree.com.au/s-property-for-rent/c18364")
saleBusiness = getTotalResultsFound("https://www.gumtree.com.au/s-business-for-sale/c18468")
saleProperty = getTotalResultsFound("https://www.gumtree.com.au/s-property-for-sale/c18367")
office = getTotalResultsFound("https://www.gumtree.com.au/s-office-space-commercial/c18365")
parking = getTotalResultsFound("https://www.gumtree.com.au/s-parking-storage/c18366")
roomshare = getTotalResultsFound("https://www.gumtree.com.au/s-roomshare/c18511")
land = getTotalResultsFound("https://www.gumtree.com.au/s-land-for-sale/c20031")
reService = getTotalResultsFound("https://www.gumtree.com.au/s-real-estate/c38467")
other = getTotalResultsFound("https://www.gumtree.com.au/s-other-real-estate/c18302")
shortTerm = getTotalResultsFound("https://www.gumtree.com.au/s-short-term/c18295")

if calculateTotalSubRE(flatShare, rent, saleBusiness, saleProperty, office, parking, roomshare, land, reService, other, shortTerm) == total :
    print("\nSub Categories in REAL ESTATE TEST")
    print("The Test Passed!")
    print("The Sum of each price type: ",
          calculateTotalSubRE(flatShare, rent, saleBusiness, saleProperty, office, parking, roomshare, land, reService,
                              other, shortTerm))
    print("The total Gumtree provided: ", total)

else:
    print("\nSub Categories in REAL ESTATE TEST")
    print("The Test Failed!")
    print("The Sum of each price type: ",
          calculateTotalSubRE(flatShare, rent, saleBusiness, saleProperty, office, parking, roomshare, land, reService,
                              other, shortTerm))
    print("The total Gumtree provided: ", total)

# ------ END OF TYPE OF REAL ESTATE ------ #

# ------ Advertisement in REAL ESTATE ------ #
premiumAds = getTotalResultsFound(url+ "?premiumAds=y")
premiumAdsResults = extractTotalIntValue(premiumAds)

featureAds = getTotalResultsFound(url+ "?featuredAds=y")
featureAdsResults = extractTotalIntValue(featureAds)

topAds = getTotalResultsFound(url+ "?gpTopAds=y")
topAdsResults = extractTotalIntValue(topAds)

highlightAds = getTotalResultsFound(url+ "?highlightAds=y")
highlightAdsResults = extractTotalIntValue(highlightAds)

urgentAds = getTotalResultsFound(url+ "?urgentAds=y")
urgentAdsResults = extractTotalIntValue(urgentAds)

priceDropAds = getTotalResultsFound(url+ "?priceDropAds=y")
priceDropAdsResults = extractTotalIntValue(priceDropAds)

# ------ STARTING ORACLE ADVERTISEMENT TEST ------- #

if calculateTotalAds(premiumAds, featureAds, topAds, highlightAds, urgentAds, priceDropAds) == total :
    print("\nAdvertisement in REAL ESTATE TEST")
    print("The Test Passed!")
    print("The Sum of each price type: ",
          calculateTotalAds(premiumAds, featureAds, topAds, highlightAds, urgentAds, priceDropAds))
    print("The total Gumtree provided: ", total)

else:
    print("\nAdvertisement in REAL ESTATE TEST")
    print("The Test Failed!")
    print("The Sum of each price type: ",
          calculateTotalAds(premiumAds, featureAds, topAds, highlightAds, urgentAds, priceDropAds))
    print("The total Gumtree provided: ", total)

# ------ END OF ORACLE ADVERTISEMENT TEST

# ------ END of Advertisement in REAL ESTATE -----