"""
This test is setting up the functions to return the total results found in the location of Wollongong NSW.
I will increment the radius of the location by its predefined options.
In theory, as the radius expands, the results found should increase.
"""
from Dans_files.testingResultsWithinRadius_ import *
import random

radius_1 = random.randint(1,500)
radius_2 = random.randint(1,500)

radius1 = getTotalResultsFound("https://www.gumtree.com.au/s-wollongong-wollongong/l3004860r" + str(radius_1))
radius1Total = extractTotalIntValue(radius1)

radius2 = getTotalResultsFound("https://www.gumtree.com.au/s-wollongong-wollongong/l3004860r" + str(radius_2))
radius2Total = extractTotalIntValue(radius2)

if radius_1 > radius_2:
    if radius1Total > radius2Total:
        print("Test has passed.")
        print("Results found for radius of", radius_1, "is:", radius1Total)
        print("Results found for radius of", radius_2, "is:", radius2Total)
    else:
        print("Test has failed.")
        print("Results found for radius of", radius_1, "is:", radius1Total)
        print("Results found for radius of", radius_2, "is:", radius2Total)
elif radius_1 == radius_2:
    if radius1Total == radius2Total:
        print("Test has passed.")
        print("Results found for radius of", radius_1, "is:", radius1Total)
        print("Results found for radius of", radius_2, "is:", radius2Total)
    else:
        print("Test has failed.")
        print("Results found for radius of", radius_1, "is:", radius1Total)
        print("Results found for radius of", radius_2, "is:", radius2Total)
else:
    if radius1Total < radius2Total:
        print("Test has passed.")
        print("Results found for radius of", radius_1, "is:", radius1Total)
        print("Results found for radius of", radius_2, "is:", radius2Total)
    else:
        print("Test has failed.")
        print("Results found for radius of", radius_1, "is:", radius1Total)
        print("Results found for radius of", radius_2, "is:", radius2Total)




