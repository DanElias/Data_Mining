
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
import time

print("getting urls...")

urls_file = open("urls.txt", "rb")
urls = pickle.load(urls_file)
urls_file.close

reviews = pd. DataFrame(columns=['restaurant_name', 'content', 'stars', 'date'])

file_delete = open('reviews.json', 'w') 
file_delete.close()

#urls = ["/biz/song-fa-bak-kut-teh-singapore-11"]

for url in urls: 

    try:
        print("scrapping: https://www.yelp.com"+url)
        if(url == "/biz/pu-dong-kitchen-singapore-2"):
            continue
        time.sleep(10)
        request = urllib.request.Request("https://www.yelp.com"+url)
        response = urllib.request.urlopen(request)
        html = response.read().decode('unicode_escape')
        soup = BeautifulSoup(html, "html.parser")
        type(soup)
        if response.getcode() != 200:
            continue
    except Exception as inst:
        continue


    reviews_content = []
    reviews_stars = []
    reviews_date_string = []
    reviews_date_datetime = []

    restaurant_name_h1 = soup.find(name="h1", attrs={"class":["lemon--h1__373c0__2ZHSL"]})
    if(restaurant_name_h1 is not None):
        restaurant_name = restaurant_name_h1.getText()

    for div in soup.find_all(name="p", attrs={"class":["comment__373c0__3EKjH"]}):
        review = div.find(name="span", attrs={"class": ["lemon--span__373c0__3997G"]})
        reviews_content.append(review.getText())

    if(len(reviews_content) == 0):
        continue

    for div in soup.find_all(name="div", attrs={"class":["i-stars__373c0__3UQrn"]}):
        reviews_stars.append(div["aria-label"])
    
    if(len(reviews_stars) < len(reviews_content)):
        continue

    for div in soup.find_all(name="span", attrs={"class":["lemon--span__373c0__3997G"]}):
        if(len(div.getText()) > 2):
            if((div.getText()[2] == '/' or div.getText()[1] == '/') and div.getText() != "14/16 Sixth Ave" and div.getText() != "80/82 Pagoda St"):
                    try:
                        reviews_date_datetime.append(datetime.strptime(div.getText(), '%m/%d/%Y'))
                    except Exception as instw:
                        continue

    i = 0
    while i < len(reviews_content):
        dictionary = dict()
        dictionary["restaurant_name"] = restaurant_name
        print("restaurant name:")
        print(dictionary["restaurant_name"])
        dictionary["content"] = reviews_content[i]
        #print("content")
        #print(dictionary["content"])
        if(i+1 < len(reviews_stars)):
            dictionary["stars"] = int(re.sub("[^0-9]", "", reviews_stars[i+1]))
            print("stars")
            print(dictionary["stars"])
        dictionary["date"] = reviews_date_datetime[i].isoformat()
        reviews = reviews.append(dictionary, ignore_index=True)
        i += 1
    
reviews.to_json(r'D:/Data_Mining/Project/reviews.json')