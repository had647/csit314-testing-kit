import requests
import re
import json
from bs4 import BeautifulSoup, SoupStrainer


# https://www.gumtree.com.au/s-keyword/k0?sort=price_asc
def generate_list(keyword, page, direction):
    url = "https://www.gumtree.com.au/s-" + keyword + "/page-" + str(page) + "/k0?sort=price_" + direction
    response = requests.get(url)

    no_top_ads = SoupStrainer(
        class_="panel search-results-page__main-ads-wrapper user-ad-collection user-ad-collection--row")
    soup = BeautifulSoup(response.text, 'html.parser', parse_only=no_top_ads)
    results_list = soup.find_all(class_="user-ad-price__price")

    results = []
    for result in results_list:
        results.append(re.findall("[-+]?\d*\.\d+|\d+", result.get_text())[0])

    return results
##