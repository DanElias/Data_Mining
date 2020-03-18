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

num_page = 24
urls = list()

while num_page < 35:
    page_url = "https://www.yelp.com/search?cflt=restaurants&find_loc=Singapore%2C+Singapore&start=" + str(num_page*30)
    urls.append(page_url)
    num_page += 1

restaurants_urls = list()

file_delete = open('restaurants.txt', 'w') 
file_delete.close()
count = 0
for url in urls: 

    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        html = response.read().decode('unicode_escape')
        soup = BeautifulSoup(html, "html.parser")
        type(soup)
        if response.getcode() != 200:
            continue
    except Exception as inst:
        continue

    for a in soup.find_all(name="a", attrs={"class":["link__373c0__1G70M"]}):
        href = a["href"]
        result = href.startswith('/biz')
        result2 =  "hrid=" not in href
        if(result and result2):
                if(len(restaurants_urls) > 0 ):
                    url = a["href"]
                    if(restaurants_urls[len(restaurants_urls)-1] != url+"?start=100"):
                        count += 1
                        print(count)
                        print("\n")
                        print("href: %s" % a["href"])
                        
                        restaurants_urls.append(a["href"])
                        restaurants_urls.append(url+"?start=20")
                        restaurants_urls.append(url+"?start=40")
                        restaurants_urls.append(url+"?start=60")
                        restaurants_urls.append(url+"?start=80")
                        restaurants_urls.append(url+"?start=100")
                        
                else:
                    count += 1
                    print(count)
                    print("\n")
                    print("href: %s" % a["href"])

                    url = a["href"]
                    restaurants_urls.append(a["href"])
                    
                    restaurants_urls.append(url+"?start=20")
                    restaurants_urls.append(url+"?start=40")
                    restaurants_urls.append(url+"?start=60")
                    restaurants_urls.append(url+"?start=80")
                    restaurants_urls.append(url+"?start=100")
                    
            

urls_file = open("urls.txt", "wb")             
pickle.dump(restaurants_urls, urls_file)
urls_file.close