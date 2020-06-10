from Master.test_Oracle_Location_ import *
from Master.test_Oracle_OfferType import *
from Master.test_Oracle_Radius import *
from Master.test_Oracle_AppropriateCategory import *
from Master.test_oracle_categoryNumbers import *
from Master.test_oracle_priceFilter import *
from Master.test_oracle_freeListings import *
from Master.test_Oracle_PriceType import *
from Master.Test_Oracle_ClothingJewellery import *
from Master.Test_Oracle_MISC import *
from Master.Test_Oracle_RealEstate import *
from Master.test_Oracle_SearchKeywords import *
from Master.test_Oracle_AppropriateCategory import *
from Master.test_Oracle_PremiumOfferTypes import *
from Master.outputCSV import *

# Here we can setup the headers once, then call all of our tests. Each test should handle the CSV output in its function.
def runAutomatedTest():
    setupCSVHeaders()
    # All test oracles go here
    run_test_location()
    run_test_radius()
    run_test_offerType()
    run_AppropriateCategory()
    run_test_CategoryNumber()
    run_test_PriceFilters()
    run_test_freeListing()
    run_test_priceType()
    run_real_estate_search_test()
    run_misc_search_test()
    run_clothing_jewellery_search_test()
    run_test_keywordSearch()
    run_test_premiumOfferType()

if __name__ == "__main__":
    runAutomatedTest()
