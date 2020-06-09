import requests
import json
from bs4 import BeautifulSoup

response = requests.get("https://www.gumtree.com.au/s-search.html")

if response:
    print("Response OK")
else:
    print("Response Failed")

print(response.status_code)

content = response.content
soup = BeautifulSoup(response.text, 'html.parser')

results_list = soup.find(class_='breadcrumbs__summary--enhanced')
print(results_list)
