
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

print("getting urls...")

urls_file = open("urls.txt", "rb")
urls = pickle.load(urls_file)
urls_file.close

reviews = pd. DataFrame(columns=['restaurant_name', 'content', 'stars', 'date'])

file_delete = open('reviews.json', 'w') 
file_delete.close()

print(urls)

for url in urls: 

    hasReviews = True
    num_page = 0

    while hasReviews:
        
        if(num_page == 0):
            print("scrapping: https://www.yelp.com"+url)
            request = urllib.request.Request("https://www.yelp.com"+url)
        else:
            print("scrapping: https://www.yelp.com"+url+"?start="+str(20*num_page))
            request = urllib.request.Request("https://www.yelp.com"+url+"?start="+str(20*num_page))
        response = urllib.request.urlopen(request)
        html = response.read().decode('unicode_escape')
        soup = BeautifulSoup(html, "html.parser")
        type(soup)

        reviews_content = []
        reviews_stars = []
        reviews_date_datetime = []

        restaurant_name_h1 = soup.find(name="h1", attrs={"class":["lemon--h1__373c0__2ZHSL"]})
        if(restaurant_name_h1 is not None):
            restaurant_name = restaurant_name_h1.getText()

        for div in soup.find_all(name="p", attrs={"class":["comment__373c0__3EKjH"]}):
            review = div.find(name="span", attrs={"class": ["lemon--span__373c0__3997G"]})
            reviews_content.append(review.getText())

        for div in soup.find_all(name="div", attrs={"class":["i-stars__373c0__3UQrn"]}):
            reviews_stars.append(div["aria-label"])

        for div in soup.find_all(name="span", attrs={"class":["lemon--span__373c0__3997G"]}):
            if(len(div.getText()) > 2):
                if(div.getText()[2] == '/' or div.getText()[1] == '/'):
                    reviews_date_datetime.append(datetime.strptime(div.getText(), '%m/%d/%Y'))

        i = 0
        while i < len(reviews_content):
            dictionary = dict()
            dictionary["restaurant_name"] = restaurant_name
            dictionary["content"] = reviews_content[i]
            if(i+1 < len(reviews_stars)):
                dictionary["stars"] = int(re.sub("[^0-9]", "", reviews_stars[i+1]))
            dictionary["date"] = reviews_date_datetime[i].isoformat()
            reviews = reviews.append(dictionary, ignore_index=True)
            i += 1

        print("Reviews text----------------")
        print(len(reviews_content))
        if(len(reviews_content) == 0):
            print("No reviews")
            hasReviews = False

        num_page += 1
    
reviews.to_json(r'D:/Data_Mining/Project/reviews.json')