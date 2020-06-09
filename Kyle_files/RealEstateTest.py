import requests
import json
from bs4 import BeautifulSoup


def extractTotalIntValue(result):
    total = int(result[0].split(" ")[0])
    return total


#### Results for FlatShare& Houseshare ####

response1 = requests.get("https://www.gumtree.com.au/s-flatshare-houseshare/c18294")

content1 = response1.content
soup1 = BeautifulSoup(response1.text, 'html.parser')

results_list1 = soup1.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for Flatshare and Houseshare in Australia: " + results_list1[0])

#### Results for Flatshare and Houseshare price < 200 ####

response2 = requests.get("https://www.gumtree.com.au/s-flatshare-houseshare/c18294?price=__200.00")

content2 = response2.content
soup2 = BeautifulSoup(response2.text, 'html.parser')

results_list2 = soup2.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for Flatshare and Houseshare in Australia which price over 300: " + results_list2[0])

#### Results for flatshare and house share price > 200 ####

response3 = requests.get("https://www.gumtree.com.au/s-flatshare-houseshare/c18294?price=200.00__")

content3 = response3.content
soup3 = BeautifulSoup(response3.text, 'html.parser')

results_list3 = soup3.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for fridges in Australia: " + results_list3[0])

if results_list2 + results_list3 == results_list1:
    print("The test has passed.")

elif results_list3 + results_list2 != results_list1:
    difference = abs((extractTotalIntValue(results_list2) + extractTotalIntValue(results_list3)) - extractTotalIntValue(results_list1))
    print("The test has failed. The difference between queries is: {0}".format(difference))


