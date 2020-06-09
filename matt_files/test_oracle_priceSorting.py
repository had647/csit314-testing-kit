from matt_files.priceSorting import generate_list

def testPriceSorting(keyword, direction):

    """
    :param keyword: Term to search.
    :param direction:  "asc" Ascending or "desc" Descending
    """

    data = generate_list(keyword, 1, direction)
    for i in range(2, 10):
        data += generate_list(keyword, i, direction)

    print(data)
    if sorted(data) == data:
        print("The price tags on the search for %s are sorted" % keyword)
    else:
        print("The price tags on the search for %s are not sorted" % keyword)


#testPriceSorting("black+car", "desc")