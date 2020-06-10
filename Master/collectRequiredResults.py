import requests
import json
from bs4 import BeautifulSoup, SoupStrainer

def getTotalResultsFound(url):
    response = requests.get(url)

    if response:
        print("Response OK")
    else:
        print("Response Failed")

    soup = BeautifulSoup(response.text, 'html.parser')
    results_list = soup.find(class_='breadcrumbs__summary--enhanced')

    result = results_list.get_text()
    return result

def extractTotalIntValue(result):
    total = int(result.split()[0])
    return total

def calculateTotalStates(act, nsw, nt, qld, sa, tas, vic, wa):
    totalFromAllStates =  act + nsw + nt + qld + sa + tas + vic + wa
    return totalFromAllStates

def calculateTotalTypes(offering, wanted):
    totalFromOfferType = offering + wanted
    return totalFromOfferType

def price_grabber(url):

    response = requests.get(url)
    content = response.content

    result_grab = BeautifulSoup(response.text, "html.parser")

    result_num = result_grab.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
#   print("Results for " + keyword + " in Australia: " + result_num)

    final_result = int(result_num[0])

    return final_result

#### Generalised method as theory ####

def keyword_checker(url):
    response = requests.get(url)
    content = response.content
    result_grab = BeautifulSoup(response.text, "html.parser")

    result_num = result_grab.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
    #   print("Results for " + keyword + " in Australia: " + result_num)

    final_result = int(result_num[0])

    return final_result

#### Generalised method as theory ####
def category_counter(url):
    response = requests.get(url)
    content = response.content
    result_grab = BeautifulSoup(response.text, "html.parser")

    result_num = result_grab.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
    #   print("Results for " + keyword + " in Australia: " + result_num)

    final_result = int(result_num[0])

    return final_result

# free listings
def generate_list(keyword):
    url = "https://www.gumtree.com.au/s-" + keyword + "/k0?price-type=free"
    response = requests.get(url)

    no_top_ads = SoupStrainer(
        class_="panel search-results-page__main-ads-wrapper user-ad-collection user-ad-collection--row")
    soup = BeautifulSoup(response.text, 'html.parser', parse_only=no_top_ads)
    results_list = soup.find_all(class_="user-ad-price__no-amount-text")

    results = []
    for result in results_list:
        results.append(result.get_text())
    return results

#### Generalised method as theory ####
def calculateTotalPriceTypes(fixed, negotiable, free, swapTrade, driveAway):
  totalFromPriceTags = fixed + negotiable + free + swapTrade + driveAway
  return totalFromPriceTags
