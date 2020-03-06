'''
    This web scraper is only used for educational purposes
'''

import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd 
import json
import re
import pickle

num_page = 0
urls = list()

while num_page < 1:
    page_url = "https://www.yelp.com/search?cflt=restaurants&find_loc=Singapore%2C+Singapore&start=" + str(num_page*30)
    urls.append(page_url)
    num_page += 1

restaurants_urls = list()

file_delete = open('restaurants.txt', 'w') 
file_delete.close()
count = 0
for url in urls: 

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read().decode('unicode_escape')
    soup = BeautifulSoup(html, "html.parser")
    type(soup)

    for a in soup.find_all(name="a", attrs={"class":["link__373c0__1G70M"]}):
        href = a["href"]
        result = href.startswith('/biz')
        result2 =  "hrid=" not in href
        if(result and result2):
            print(count)
            print("\n")
            print("href: %s" % a["href"])
            count += 1
            restaurants_urls.append(a["href"])

urls_file = open("urls.txt", "wb")             
pickle.dump(restaurants_urls, urls_file)
urls_file.close