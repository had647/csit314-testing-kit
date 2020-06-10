from Master.outputCSV import outputCSV
from Master.collectRequiredResults import *


def run_test_CategoryNumber():
    print("\nRunning Category Test Oracle now...")
    general = generalSearch()
    print("The number of results for listings in Australia are: " + str(general))
    category = categorySearch()
    print("The number of results of all categories combined in Australia are: " + str(category))

    category_testCase = "Results displayed from all Australia vs the sum of all category listings"

    if category == general:
        print("The search query is acting as expected.")
        outputCSV(category_testCase, True, general, category)

    elif category != general:
        total = general - category
        print("The estimated result did not equate to the true result. The difference between queries is: "
              + str(total))
        outputCSV(category_testCase, False, general, category)

        #yeboi

def categorySearch():

    category_list = ["home-garden", "cars-vans-utes", "clothing-jewellery", "baby-children","electronics-computer",
        "antiques-art-collectables", "books-music-games", "miscellaneous-goods", "sport-fitness", "services-for-hire",
        "pets", "real-estate", "jobs", "boats-jet-skis", "community", "tickets"]

    category_code_list = ["c18397", "c18320", "c18308","c18318", "c20045", "c18297", "c18393", "c18319", "c18314",
                          "c9303", "c18433", "c9296", "c9302", "c18420", "c9300", "c18361"]

    list_num = 0;
    category_num = 0;

    for x in category_list:

        url = "https://www.gumtree.com.au/s-" + category_list[list_num] + "/k0" + category_code_list[list_num]
        category_num += category_counter(url)

        list_num += 1

    return category_num



def generalSearch():

    url = "https://www.gumtree.com.au/s-search.html"
    generalPriceResults = keyword_checker(url)

    return generalPriceResults



