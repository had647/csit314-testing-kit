from Master.outputCSV import outputCSV
from lw803_files.result_getter import keyword_checker

def run_AppropriateCategory():
    def testCategoryAppropriateness():

        categoryAppropriateness("ugg boots", "cars-vans-utes", "c18320")
        categoryAppropriateness("ugg boots", "home-garden", "c18397")
        categoryAppropriateness("ugg boots", "jobs", "c9302")
        categoryAppropriateness("ugg boots", "real-estate", "c9296")
        categoryAppropriateness("ugg boots", "books-music-games", "c18393")
        categoryAppropriateness("ugg boots",  "clothing-jewellery", "c18308")

    def categoryAppropriateness(randomKeyword, randomCategory, catCode):



        keyword = randomKeyword
        category = randomCategory
        general = generalSearch(keyword)
        print("The number of results for keyword " + keyword + " in Australia are: " + str(general))
        wrong = wrongCategorySearch(keyword, category, catCode)
        print("The number of results for keyword " + keyword + " in category " + category +
              " in Australia are: " + str(wrong))

        category_testcase = "Results displayed for " + keyword + " in all categories vs results displayed for " + keyword + " in " + category + "."

        if wrong == 0:
            print("The search query is acting as expected.")
            outputCSV(category_testcase, True, 0, wrong)

        elif wrong > 0:
            print("The number of results for " + keyword + " are " + str(general) +
                  ". However, it should not be found in the category " + category + ". This is not the case.")
            outputCSV(category_testcase, False, 0, wrong)

    def wrongCategorySearch(keyword, category,catCode):

        url = "https://www.gumtree.com.au/s-" + category + "/" + queryBuilder(keyword) + "/k0" + catCode
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




