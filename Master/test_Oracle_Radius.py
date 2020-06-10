"""
This test is setting up the functions to return the total results found in the location of Wollongong NSW.
Radius is chosen randomly.
In theory, as the radius expands, the results found should increase.
"""
from Master.collectRequiredResults import *
from Master.outputCSV import *
import random

def run_test_radius():
    print("\nRunning Radius Test Oracle now...")

    # Run 5 different tests with new random parameters each time.
    for i in range(5):
        radius_1 = random.randint(1,250)
        radius_2 = radius_1 + 5

        radius1 = getTotalResultsFound("https://www.gumtree.com.au/s-wollongong-wollongong/l3004860r" + str(radius_1))
        radius1Total = extractTotalIntValue(radius1)

        radius2 = getTotalResultsFound("https://www.gumtree.com.au/s-wollongong-wollongong/l3004860r" + str(radius_2))
        radius2Total = extractTotalIntValue(radius2)

        # Preparing Variables for output
        testCase = "Results Displayed when radius of location is altered with radius being "
        expectedResult = str(radius1Total) + "+"

        if radius_1 > radius_2:
            if radius1Total > radius2Total:
                print("Test has passed.")
                print("Results found for radius of", radius_1, "is:", radius1Total)
                print("Results found for radius of", radius_2, "is:", radius2Total)
                outputCSV(testCase + str(radius_1), str(radius_2), True, expectedResult, radius2Total)
            else:
                print("Test has failed.")
                print("Results found for radius of", radius_1, "is:", radius1Total)
                print("Results found for radius of", radius_2, "is:", radius2Total)
                outputCSV(testCase + str(radius_1) + " and " + str(radius_2), False, expectedResult, radius2Total)
        elif radius_1 == radius_2:
            if radius1Total == radius2Total:
                print("Test has passed.")
                print("Results found for radius of", radius_1, "is:", radius1Total)
                print("Results found for radius of", radius_2, "is:", radius2Total)
                outputCSV(testCase + str(radius_1) + " and " + str(radius_2), True, expectedResult, radius2Total)
            else:
                print("Test has failed.")
                print("Results found for radius of", radius_1, "is:", radius1Total)
                print("Results found for radius of", radius_2, "is:", radius2Total)
                outputCSV(testCase + str(radius_1) + " and " + str(radius_2), False, expectedResult, radius2Total)
        else:
            if radius1Total < radius2Total:
                print("Test has passed.")
                print("Results found for radius of", radius_1, "is:", radius1Total)
                print("Results found for radius of", radius_2, "is:", radius2Total)
                outputCSV(testCase + str(radius_1) + " and " + str(radius_2), True, expectedResult, radius2Total)
            else:
                print("Test has failed.")
                print("Results found for radius of", radius_1, "is:", radius1Total)
                print("Results found for radius of", radius_2, "is:", radius2Total)
                outputCSV(testCase + str(radius_1) + " and " + str(radius_2), False, expectedResult, radius2Total)

