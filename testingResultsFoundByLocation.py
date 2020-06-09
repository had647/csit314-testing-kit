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

def main():
    australia = getTotalResultsFound("https://www.gumtree.com.au/s-search.html")
    totalAus = extractTotalIntValue(australia)

    act = getTotalResultsFound("https://www.gumtree.com.au/s-act/l3008838")
    totalACT = extractTotalIntValue(act)

    nsw = getTotalResultsFound("https://www.gumtree.com.au/s-nsw/l3008839")
    totalNSW = extractTotalIntValue(nsw)

    nt = getTotalResultsFound("https://www.gumtree.com.au/s-nt/l3008840")
    totalNT = extractTotalIntValue(nt)

    qld = getTotalResultsFound("https://www.gumtree.com.au/s-qld/l3008841")
    totalQLD = extractTotalIntValue(qld)

    sa = getTotalResultsFound("https://www.gumtree.com.au/s-sa/l3008842")
    totalSA = extractTotalIntValue(sa)

    tas = getTotalResultsFound("https://www.gumtree.com.au/s-tas/l3008843")
    totalTAS = extractTotalIntValue(tas)

    vic = getTotalResultsFound("https://www.gumtree.com.au/s-vic/l3008844")
    totalVIC = extractTotalIntValue(vic)

    wa = getTotalResultsFound("https://www.gumtree.com.au/s-wa/l3008845")
    totalWA = extractTotalIntValue(wa)

    if calculateTotal(totalACT, totalNSW, totalNT, totalQLD, totalSA, totalTAS, totalVIC, totalWA) == totalAus:
        print("The results are equal")
    else:
        print("Gumtree did a whoopsie")


if __name__== "__main__":
    main()