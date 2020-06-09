from lw803_files.appropriateCategory import *

def testCategoryAppropriateness(randomKeyword, randomCategory):

    keyword = randomKeyword
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

    url = "https://www.gumtree.com.au/s-" + category + "/" + queryBuilder(keyword) + "/k0c18320"
    underPriceResults = keyword_checker(url)

    return underPriceResults

def generalSearch(keyword):

    url = "https://www.gumtree.com.au/s-" + queryBuilder(keyword) + "/k0"
    generalPriceResults = keyword_checker(url)

    return generalPriceResults

def queryBuilder(keywordToChange):

    if " " in keywordToChange:

        tempKeyword = keywordToChange.split(" ")
        updatedKeyword = tempKeyword[0] + "+" + tempKeyword[1]

        return updatedKeyword

    else:
        return keywordToChange




