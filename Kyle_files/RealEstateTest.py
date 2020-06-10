import requests
import json
from bs4 import BeautifulSoup


def getTotalResultsFound(url):
    response = requests.get(url)

    if response:
        print("Real Estate Gumtree URL Response OK")

    else:
        print("Real Estate Gumtree URL Response Failed")

    soup = BeautifulSoup(response.text, 'html.parser')
    results_list = soup.find(class_='breadcrumbs__summary--enhanced')

    result = results_list.get_text()
    return result

# ---- Calculate total of advertisement type of Real Estate
def calculateTotalAds(premiumAdsResults, featureAdsResults, topAdsResults, highlightAdsResults, urgentAdsResults, priceDropAdsResults):
  totalAdsRealEstate = premiumAdsResults, featureAdsResults, topAdsResults, highlightAdsResults, urgentAdsResults, priceDropAdsResults
  return totalAdsRealEstate

# ----- Calculate total of sub categories of Real Estate
def calculateTotalSubRE(flatshare, rent, saleBusiness, saleProperty, office, parking, roomshare, land, reService, other, shortTerm):
    totalAdsRealEstate = flatshare, rent, saleBusiness, saleProperty, office, parking, roomshare, land, reService, other, shortTerm
    return totalAdsRealEstate


def extractTotalIntValue(result):
    total = int(result[0].split(" ")[0])
    return total


