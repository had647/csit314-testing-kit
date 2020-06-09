from lw803_files.priceFilter import *

def testPriceFilters():

    keyword = "boat" # to be random
    over = overSetPrice(keyword)
    print("The number of results for " + keyword + "in Australia above $5,000.00 are: " + str(over))
    under = underSetPrice(keyword)
    print("The number of results for " + keyword + "in Australia under $5,000.00 are: " + str(under))
    general = generalSearch(keyword)
    print("The number of results for " + keyword + "in Australia: " + str(general))

    if over + under == general:
        print("The estimated result did equate to the true result.")

    elif over + under != general:
        total = general - (under + over)
        print("The estimated result did not equate to the true result. The difference between queries is: " + str(total))


def overSetPrice(keyword):

    url = "https://www.gumtree.com.au/s-" + keyword + "/k0?price=5000.00__"
    overPriceResults = price_grabber(url, keyword)

    return overPriceResults

def underSetPrice(keyword):

    url = "https://www.gumtree.com.au/s-" + keyword + "/k0?price=__5000.00"
    underPriceResults = price_grabber(url, keyword)

    return underPriceResults

def generalSearch(keyword):

    url = "https://www.gumtree.com.au/s-" + keyword + "/k0"
    generalPriceResults = price_grabber(url, keyword)

    return generalPriceResults