from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_test_freeListing():
    print("\nRunning Free Listing Test Oracle now...")

    keyword = "black+car"
    data = generate_list(keyword)

    testCase = "Results displayed for refined free searches compared to their actual price listing"
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
