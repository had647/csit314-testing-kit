from Denver_files.testingResultsFoundBySearch import *

### This will test to see if adding keywords to a search will lower the amount of results ###

total = getTotalResultsFound("https://www.gumtree.com.au/s-search.html")
totalResults = extractTotalIntValue(total)

searchOne = getTotalResultsFound("https://www.gumtree.com.au/s-car/k0")
searchOneTotal = extractTotalIntValue(searchOne)

searchTwo = getTotalResultsFound("https://www.gumtree.com.au/s-car+mitsubishi/k0")
searchTwoTotal = extractTotalIntValue(searchTwo)

searchThree = getTotalResultsFound("https://www.gumtree.com.au/s-car+mitsubishi+trailer/k0")
searchThreeTotal = extractTotalIntValue(searchThree)

hasFailed = False

if searchOneTotal > totalResults :
  hasFailed = True

elif searchTwoTotal > searchOneTotal :
  hasFailed = True

elif searchThreeTotal > searchTwoTotal :
  hasFailed = True

if hasFailed == False :
    print("\nThe Test Passed!")
    print("The total results: ",
          totalResults)
    print("Search 1 results: ",
          searchOneTotal)
    print("Search 2 results: ",
          searchTwoTotal)
    print("Search 3 results: ",
          searchThreeTotal)

else:
    print("\nThe Test Failed!")
    print("The total results: ",
          totalResults)
    print("Search 1 results: ",
          searchOneTotal)
    print("Search 2 results: ",
          searchTwoTotal)
    print("Search 3 results: ",
          searchThreeTotal)

