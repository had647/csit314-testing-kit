import requests
import json
from bs4 import BeautifulSoup


def getTotalResultsFound(url):
    response = requests.get(url)

    if response:
        print("MISC URL Response OK")

    else:
        print("MISC URL Response Failed")

    soup = BeautifulSoup(response.text, 'html.parser')
    results_list = soup.find(class_='breadcrumbs__summary--enhanced')

    result = results_list.get_text()
    return result

def calculateTotalOFFER(offering, wanted):
  totalOfferMISCGOODS = offering + wanted
  return totalOfferMISCGOODS



def extractTotalIntValue(result):
    total = int(result.split()[0])
    return total


