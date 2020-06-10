from Master.collectRequiredResults import generate_list
from Master.outputCSV import *

def testFreeListings(keyword):

    data = generate_list(keyword)

    testCase = "Results displayed for free marked searches compared to their actual price listing"
    not_free_flag = False
    for price in data:
        if price != "Free":
            not_free_flag = True

    if not_free_flag:
        print("Non-free listing appearing in results")
        outputCSV(testCase, False, "Free", "Not Free")
    else:
        print("All listings are free")
        outputCSV(testCase, True, "Free", "Free")

testFreeListings("black+car")