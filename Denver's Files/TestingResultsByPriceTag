import requests
import json
from bs4 import BeautifulSoup

def extractTotalIntValue(result):
        total = int(result[0].split(" ")[0])
        return total

#### Results for fridges with a fixed price ####

response1 = requests.get("https://www.gumtree.com.au/s-fridge/k0?price-type=fixed")

content1 = response1.content
soup1 = BeautifulSoup(response1.text, 'html.parser')

results_list1 = soup1.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for fridges with a fixed price: " + results_list1[0])


#### Results for fridges tagged as free ####

response2 = requests.get("https://www.gumtree.com.au/s-fridge/k0?price-type=free")

content2 = response2.content
soup2 = BeautifulSoup(response2.text, 'html.parser')

results_list2 = soup2.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for fridges tagged as free: " + results_list2[0])


#### Results for fridges with no price type filter ####

response3 = requests.get("https://www.gumtree.com.au/s-fridge/k0")

content3 = response3.content
soup3 = BeautifulSoup(response3.text, 'html.parser')

results_list3 = soup3.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for fridges in Australia: " + results_list3[0])


if results_list1 + results_list2  == results_list3:
    print("The test has passed.")

elif results_list1 + results_list2 != results_list3:
    difference = abs(extractTotalIntValue(results_list2) - extractTotalIntValue(results_list1))
    print("The test has failed. The difference between queries is: {0}".format(difference))
    
    #I need to find the values of the other tags
    # THIS IS STILL A WIP
