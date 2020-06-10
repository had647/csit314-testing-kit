from lw803_files.result_getter import price_grabber


def testPriceFilters():


    over = overSetPrice()
    print("The number of results for in Australia above $5,000.00 are: " + str(over))
    under = underSetPrice()
    print("The number of results for keyword in Australia under $5,000.00 are: " + str(under))
    general = generalSearch()
    print("The number of results for in Australia: " + str(general))

    if over + under == general:
        print("The estimated result did equate to the true result.")

    elif over + under != general:
        total = general - (under + over)
        print("The estimated result did not equate to the true result. The difference between queries is: " + str(total))

# def testPriceFilters(randomKeyword):
#
#     keyword = randomKeyword
#     over = overSetPrice(keyword)
#     print("The number of results for " + keyword + "in Australia above $5,000.00 are: " + str(over))
#     under = underSetPrice(keyword)
#     print("The number of results for keyword " + keyword + "in Australia under $5,000.00 are: " + str(under))
#     general = generalSearch(keyword)
#     print("The number of results for " + keyword + "in Australia: " + str(general))
#
#     if over + under == general:
#         print("The estimated result did equate to the true result.")
#
#     elif over + under != general:
#         total = general - (under + over)
#         print("The estimated result did not equate to the true result. The difference between queries is: " + str(total))


# def overSetPrice(keyword):
#
#     url = "https://www.gumtree.com.au/s-" + keyword + "/k0?price=5000.00__"
#     overPriceResults = price_grabber(url, keyword)
#
#     return overPriceResults
#
# def underSetPrice(keyword):
#
#     url = "https://www.gumtree.com.au/s-" + keyword + "/k0?price=__5000.00"
#     underPriceResults = price_grabber(url, keyword)
#
#     return underPriceResults
#
# def generalSearch(keyword):
#
#     url = "https://www.gumtree.com.au/s-" + keyword + "/k0"
#     generalPriceResults = price_grabber(url, keyword)
#
#     return generalPriceResults

def overSetPrice():

    url = "https://www.gumtree.com.au/s-ads?price=5000.00__"
    overPriceResults = price_grabber(url)

    return overPriceResults

def underSetPrice():

    url = "https://www.gumtree.com.au/s-ads?price=__5000.00"
    underPriceResults = price_grabber(url)

    return underPriceResults

def generalSearch():

    url = "https://www.gumtree.com.au/s-search.html"
    generalPriceResults = price_grabber(url)

    return generalPriceResults