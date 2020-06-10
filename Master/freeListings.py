import requests
import re
import json
from bs4 import BeautifulSoup, SoupStrainer

# https://www.gumtree.com.au/s-keyword/k0?price-type=free
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


if __name__ == "__main__":
    res = generate_list("black+car")
    print(res)