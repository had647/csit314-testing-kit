from Dans_files.test_Oracle_Location_ import *
from Dans_files.test_Oracle_OfferType import *
from Dans_files.test_Oracle_Radius import *
from Dans_files.outputCSV import *

# Here we can setup the headers once, then call all of our tests. Each test should handle the CSV ouput in its function.
def runAutomatedTest():
    setupCSVHeaders()
    # All test oracles go here
    run_test_location()
    run_test_radius()
    run_test_offerType()


if __name__ == "__main__":
    runAutomatedTest()

