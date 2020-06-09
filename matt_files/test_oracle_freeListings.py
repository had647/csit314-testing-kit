from matt_files.freeListings import generate_list

def testFreeListings(keyword):

    data = generate_list(keyword)

    not_free_flag = False
    for price in data:
        if price != "Free":
            not_free_flag = True

    if not_free_flag:
        print("Non-free listing appearing in results")
    else:
        print("All listings are free")


testFreeListings("black+car")