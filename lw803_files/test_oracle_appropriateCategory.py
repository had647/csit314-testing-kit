from lw803_files.appropriateCategory import *
import re

def testCategoryAppropriateness(randomKeyword, randomCategory):

    keyword = randomKeyword
    keyword.replace(" ", "+")
    category = randomCategory
    general = generalSearch(keyword)
    print("The number of results for keyword " + keyword + " in Australia are: " + str(general))
    wrong = wrongCategorySearch(keyword, category)
    print("The number of results for keyword " + keyword + " in category " + category +
          " in Australia are: " + str(wrong))

    if wrong == 0:
        print("The search query is acting as expected.")

    elif wrong > 0:
        print("The number of results for " + keyword + " are " + str(general) +
              ". However, it should not be found in the category " + category + ". This is not the case.")

def wrongCategorySearch(keyword, category):
    print(keyword)
    url = "https://www.gumtree.com.au/s-" + category + "/" + queryBuilder(keyword) + "/k0c18320"
    underPriceResults = keyword_checker(url)

    return underPriceResults

def generalSearch(keyword):

    url = "https://www.gumtree.com.au/s-" + keyword + "/k0"
    generalPriceResults = keyword_checker(url)

    return generalPriceResults

def queryBuilder(keyword):

    string = keyword.split()
    string2 = string[0] + "+" + string[1]

    return string2


