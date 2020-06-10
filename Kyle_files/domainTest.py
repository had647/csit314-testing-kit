from Kyle_files.Test_Oracle_MISC import *
from Kyle_files.Test_Oracle_RealEstate import *
from Kyle_files.Test_Oracle_ClothingJewellery import *
from Kyle_files.outputCSV import *

def runAutomatedTest():
    setupCSVHeaders()
    # All test oracles go here
    real_estate_search_test()
    misc_search_test()
    clothing_jewellery_search_test()


if __name__ == "__main__":
    runAutomatedTest()
