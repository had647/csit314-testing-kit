# Import the following libraries to retrieve a HTML page and then conduct
# data pulling via BeautifulSoup
from requests.exceptions import HTTPError
import requests
from bs4 import BeautifulSoup

def getTotalResultsFound(url):
    response = None
    try:
        response = requests.get(url)
    except ConnectionError as ConnErr:
        print("Encountered an error while trying to retrieve webpage from the following URL: \n" + url)
        print("\n\nERROR: No response from host")
    except Exception as Excp:
        print("Encountered an error while trying to retrieve webpage from the following URL: \n" + url)
        print("\n\nERROR: Unknown Exception")
    except BaseException as BaseExcp:
        print("Encountered an error while trying to retrieve webpage from the following URL: \n" + url)
        print("\n\nERROR: Unknown BaseException")
    if response:
        print("==================\n*Response Success*\n==================\n")
        print("URL: " + url + "\n")
        print("Response Code: " + str(response.status_code) + "\n")
    else:
        print("=================\n*Response Failed*\n=================\n")
        print("URL: " + url + "\n")
        print("Response Code: " + response.status_code + "\n")
    soup = BeautifulSoup(response.text, 'html.parser')
    results_list = soup.find(class_='breadcrumbs__summary--enhanced')
    result = results_list.get_text()
    return result

def extractTotalIntValue(result):
    total = int(result.split()[0])
    return total