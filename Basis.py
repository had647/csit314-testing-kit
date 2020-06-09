import requests
import json
from bs4 import BeautifulSoup

def getTotalResultsFound(url):
    response = requests.get(url)

    if response:
        print("Response OK")
    else:
        print("Response Failed")

    soup = BeautifulSoup(response.text, 'html.parser')
    results_list = soup.find(class_='breadcrumbs__summary--enhanced')

    result = results_list.get_text()

    # Getting the int value of result
    total = int(result.split()[0])

    return result

def extractTotalIntValue(result):
    total = int(result.split()[0])
    return total

if __name__ == "__main__":
    result = getTotalResultsFound("https://www.gumtree.com.au/s-act/l3008838")
    total = extractTotalIntValue(result)

    print(result)
    print(total)