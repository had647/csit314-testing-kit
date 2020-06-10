# Import the following libraries to retrieve a HTML page and then conduct
# data pulling via BeautifulSoup
from requests.exceptions import HTTPError
import requests
from bs4 import BeautifulSoup

def requestWebpage(url):
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