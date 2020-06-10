from Master.outputCSV import outputCSV
from Master.priceSorting import generate_list

def testPriceSorting():
    print("Running Price Sorting Test Oracle now...")

    keyword = "black+car"
    direction = "desc"

    data = generate_list(keyword, 1, direction)
    for i in range(2, 10):
        data += generate_list(keyword, i, direction)

    testcase_priceSorting = "Results are displayed in descending price"

    if sorted(data) == data:
        print("The price tags on the search for %s are sorted" % keyword)
        outputCSV(testcase_priceSorting, True, "Sorted", "Sorted")

    else:
        print("The price tags on the search for %s are not sorted" % keyword)
        outputCSV(testcase_priceSorting, False, "Sorted", "Unsorted")

##