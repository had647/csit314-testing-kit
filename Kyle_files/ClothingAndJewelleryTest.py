import requests
import json
from bs4 import BeautifulSoup


def getTotalResultsFound(url):
    response = requests.get(url)

    if response:
        print("Clothing & Jewellery URL Response OK")

    else:
        print("Clothing & Jewellery URL Response Failed")

    soup = BeautifulSoup(response.text, 'html.parser')
    results_list = soup.find(class_='breadcrumbs__summary--enhanced')

    result = results_list.get_text()
    return result

def calculateTotalCategories(women, jewellery, womenShoes, men, bags, menShoes, dressMaking):
  totalCategories = women + jewellery + womenShoes + men + bags + menShoes + dressMaking
  return totalCategories


def extractTotalIntValue(result):
    total = int(result[0].split(" ")[0])
    return total


