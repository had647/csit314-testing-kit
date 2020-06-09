import requests
import json
from bs4 import BeautifulSoup

#### Results for boats under $5k ####

response1 = requests.get("https://www.gumtree.com.au/s-boat/k0?price=5000.00__")

content1 = response1.content
soup1 = BeautifulSoup(response1.text, 'html.parser')

results_list1 = soup1.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for boats $5000 or above in Australia: " + results_list1[0])


#### Results for boats over 5k ####

response2 = requests.get("https://www.gumtree.com.au/s-boat/k0?price=__5000.00")

content2 = response2.content
soup2 = BeautifulSoup(response2.text, 'html.parser')

results_list2 = soup2.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for boats $5000 or below in Australia: " + results_list2[0])


#### Results for boats with no price filter ####

response3 = requests.get("https://www.gumtree.com.au/s-boat/k0")

content3 = response3.content
soup3 = BeautifulSoup(response3.text, 'html.parser')

results_list3 = soup3.find(class_='breadcrumbs__summary--enhanced').contents[0].split(":")
print("Results for boats in Australia: " + results_list3[0])


if results_list1 + results_list2  == results_list3:
    print("The test has passed.")

elif results_list1 + results_list2 != results_list3:
    difference = results_list2 - results_list1
    print("The test has failed. The difference between quries is: " + difference)


def extractTotalIntValue(result):
        total = int(result.split()[0])
        return total