import requests
import json
from bs4 import BeautifulSoup


#### Generalised method as theory ####

def keyword_checker(url):
    response = requests.get(url)
    content = response.content
    result_grab = BeautifulSoup(response.text, "html.parser")

    result_num = result_grab.find(class_='breadcrumbs__summary--enhanced').contents[0].split(" ")
    #   print("Results for " + keyword + " in Australia: " + result_num)

    final_result = int(result_num[0])

    return final_result

