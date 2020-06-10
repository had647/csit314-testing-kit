# Does the total listing of Australia match the total sum of all states' listings?
from Master.collectRequiredResults import *
from Master.outputCSV import *

def run_test_location():
    print("\nRunning Location Test Oracle now...")

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

    # Preparing variables for output
    totalAllStates = calculateTotalStates(totalACT, totalNSW, totalNT, totalQLD, totalSA, totalTAS, totalVIC, totalWA)
    testCase = "Results displayed from all Australia vs the sum of all states"

    if totalAllStates == totalAus:
        print("\nThe Test Passed!")
        print("The Sum of each state: ",
              totalAllStates)
        print("The total Gumtree provided: ", totalAus)
        outputCSV(testCase, True, totalAus, totalAllStates)
    else:
        print("\nThe Test Failed!")
        print("The Sum of each state: ",
              totalAllStates)
        print("The total Gumtree provided: ", totalAus)
        outputCSV(testCase, False, totalAus, totalAllStates)

