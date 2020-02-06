
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re

url = "https://www.yelp.com/biz/soup-nutsy-toronto?page_src=related_bizes"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read().decode('unicode_escape')
soup = BeautifulSoup(html, "html.parser")

reviews_content = []
reviews_stars = []
reviews_date_string = []
reviews_date_datetime = []

for div in soup.find_all(name="p", attrs={"class":["comment__373c0__3EKjH"]}):
    review = div.find(name="span", attrs={"class": ["lemon--span__373c0__3997G"]})
    reviews_content.append(review.getText())

for div in soup.find_all(name="div", attrs={"class":["i-stars__373c0__3UQrn"]}):
    reviews_stars.append(div["aria-label"])

for div in soup.find_all(name="span", attrs={"class":["lemon--span__373c0__3997G"]}):
    if(len(div.getText()) > 2):
        if(div.getText()[2] == '/' or div.getText()[1] == '/'):
            reviews_date_string.append(div.getText())
            reviews_date_datetime.append(datetime.strptime(div.getText(), '%m/%d/%Y'))

i = 0
reviews = dict()
while i < len(reviews_content):
    dictionary = dict()
    dictionary["content"] = reviews_content[i]
    dictionary["stars"] = int(re.sub("[^0-9]", "", reviews_stars[i+1]))
    dictionary["date"] = reviews_date_datetime[i].isoformat()
    dictionary["date_string"] = reviews_date_string[i]
    reviews[i] = dictionary
    i += 1

with open('reviews.txt', 'a') as file:
     file.write(json.dumps(reviews)) 
