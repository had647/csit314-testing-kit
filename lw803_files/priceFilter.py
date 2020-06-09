import requests
import json
from bs4 import BeautifulSoup

# #### Results for boats under $5k ####
#
# response1 = requests.get("https://www.gumtree.com.au/s-boat/k0?price=5000.00__")
#
# content1 = response1.content
# soup1 = BeautifulSoup(response1.text, 'html.parser')
#
# results_list1 = soup1.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
# result1 = int(results_list1[0])
# print("Results for boats $5000 or above in Australia: " + str(result1))
# 
#
# #### Results for boats over 5k ####
#
# response2 = requests.get("https://www.gumtree.com.au/s-boat/k0?price=__5000.00")
#
# content2 = response2.content
# soup2 = BeautifulSoup(response2.text, 'html.parser')
#
# results_list2 = soup2.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
# result2 = int(results_list2[0])
# print("Results for boats $5000 or below in Australia: " + str(result2))
#
#
# #### Results for boats with no price filter ####
#
# response3 = requests.get("https://www.gumtree.com.au/s-boat/k0")
#
# content3 = response3.content
# soup3 = BeautifulSoup(response3.text, 'html.parser')
#
# results_list3 = soup3.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
# result3 = int(results_list3[0])
# print("Results for boats in Australia: " + str(result3))
#
#
# if result1 + result2 == result3:
#     print("The test has passed.")
#
# elif result1 + result2 != result3:
#     difference = result3 - (result2 + result1)
#     print("The test has failed. The difference between quries is: " + str(difference))

#
# def extractTotalIntValue(result):
#         total = int(result.split()[0])
#         return total


#### Generalised method as theory ####

def price_grabber(url, keyword):

    response = requests.get(url)
    content = response.content
    result_grab = BeautifulSoup(response.text, "html.parser")

    result_num = result_grab.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
#    print("Results for " + keyword + " in Australia: " + result_num)

    final_result = int(result_num[0])

    return final_result




