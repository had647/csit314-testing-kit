"""
This test is setting up the functions to return the total results found in the location of Wollongong NSW.
I will increment the radius of the location by its predefined options.
In theory, as the radius expands, the results found should increase.
"""

import requests
import json
from bs4 import BeautifulSoup

def getTotalResultsFound(url):
    response = requests.get(url)

    if response:
        print("Response OK")
    else:
        print("Response Failed")

    soup = BeautifulSoup(response.text, 'html.parser')
    results_list = soup.find(class_='breadcrumbs__summary--enhanced')

    result = results_list.get_text()
    return result

def extractTotalIntValue(result):
    total = int(result.split()[0])
    return total

def calculateTotal(act, nsw, nt, qld, sa, tas, vic, wa):
    totalFromAllStates =  act + nsw + nt + qld + sa + tas + vic + wa
    return totalFromAllStates

zeroKM = getTotalResultsFound("https://www.gumtree.com.au/s-wollongong-wollongong/l3004860")
oneKMTotal = extractTotalIntValue(zeroKM)

twoKM = getTotalResultsFound("https://www.gumtree.com.au/s-wollongong-wollongong/l3004860r2")
twoKMTotal = extractTotalIntValue(twoKM)



