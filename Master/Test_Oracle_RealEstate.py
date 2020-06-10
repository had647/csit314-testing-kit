"""
This oracle will compare the total of test result equals the original result
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_real_estate_search_test():
        print("\nRunning Subcategories Real Estate Test Oracle now...")

        keyword = "real-estate"
        url = "https://www.gumtree.com.au/s-" + keyword + "/c9296"

        total = getTotalResultsFound(url)
        totalResults = extractTotalIntValue(total)

        # ------ TYPE of REAL ESTATE  ------- #

        flatShare = getTotalResultsFound("https://www.gumtree.com.au/s-flatshare-houseshare/c18294")
        flatShareResult = extractTotalIntValue(flatShare)
        rent = getTotalResultsFound("https://www.gumtree.com.au/s-property-for-rent/c18364")
        rentResult = extractTotalIntValue(rent)
        saleBusiness = getTotalResultsFound("https://www.gumtree.com.au/s-business-for-sale/c18468")
        saleBusinessResult = extractTotalIntValue(saleBusiness)
        saleProperty = getTotalResultsFound("https://www.gumtree.com.au/s-property-for-sale/c18367")
        salePropertyResult = extractTotalIntValue(saleProperty)
        office = getTotalResultsFound("https://www.gumtree.com.au/s-office-space-commercial/c18365")
        officeResult = extractTotalIntValue(office)
        parking = getTotalResultsFound("https://www.gumtree.com.au/s-parking-storage/c18366")
        parkingResult = extractTotalIntValue(parking)
        roomshare = getTotalResultsFound("https://www.gumtree.com.au/s-roomshare/c18511")
        roomshareResult = extractTotalIntValue(roomshare)
        land = getTotalResultsFound("https://www.gumtree.com.au/s-land-for-sale/c20031")
        landResult = extractTotalIntValue(land)
        reService = getTotalResultsFound("https://www.gumtree.com.au/s-real-estate/c38467")
        reServiceResult = extractTotalIntValue(reService)
        other = getTotalResultsFound("https://www.gumtree.com.au/s-other-real-estate/c18302")
        otherResult = extractTotalIntValue(other)
        shortTerm = getTotalResultsFound("https://www.gumtree.com.au/s-short-term/c18295")
        shortTermResult = extractTotalIntValue(shortTerm)
        testCase = "Results displayed for Real Estate in Australia and its categories in Australia"

        totalAllCategories = calculateTotalSubRE(flatShareResult, rentResult, saleBusinessResult, salePropertyResult, officeResult, parkingResult, roomshareResult, landResult, reServiceResult, otherResult, shortTermResult)
        if  totalAllCategories == total :
            print("\nSub Categories in REAL ESTATE TEST")
            print("The Test Passed!")
            print("The Sum of each price type: ",
                  totalAllCategories)
            print("The total Gumtree provided: ", totalResults)
            outputCSV(testCase, True, totalResults, totalAllCategories)
        else:
            print("\nSub Categories in REAL ESTATE TEST")
            print("The Test Failed!")
            print("The Sum of each price type: ",
                  totalAllCategories)
            print("The total Gumtree provided: ", totalResults)
            outputCSV(testCase, False, totalResults, totalAllCategories)

        # ------ END OF TYPE OF REAL ESTATE ------ #

        # ------ Advertisement in REAL ESTATE ------ #

        print("\nRunning Advertisement Real Estate Test Oracle now...")
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

        testCase = "Results displayed in Real Estate in Australia and its advertisement type in Australia"

        totalAds = calculateTotalAds(premiumAdsResults, featureAdsResults, topAdsResults, highlightAdsResults, urgentAdsResults, priceDropAdsResults)
            # ------ STARTING ORACLE ADVERTISEMENT TEST ------- #

        if  totalAds == totalAds :
            print("\nAdvertisement in REAL ESTATE TEST")
            print("The Test Passed!")
            print("The Sum of each price type: ",
                  totalAds)
            print("The total Gumtree provided: ", totalAds)
            outputCSV(testCase, True, totalAds, totalAds)

        else:
            print("\nAdvertisement in REAL ESTATE TEST")
            print("The Test Failed!")
            print("The Sum of each price type: ",
                  totalAds)
            print("The total Gumtree provided: ", totalAds)
            outputCSV(testCase, False, totalAds, totalAds)

            # ------ END OF ORACLE ADVERTISEMENT TEST

        # ------ END of Advertisement in REAL ESTATE -----