import csv
import re
import nltk
import sys
import getopt
import pickle
from nltk import stem
import math

file = open("sentences.csv", "w", encoding="utf8", newline='')
writer = csv.writer(file)

with open('yelp_singapore_restaurants_reviews.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        restaurant = row[0]
        review = row[1]
        stars = row[2]
        date = row[3]
        sentences = nltk.tokenize.sent_tokenize(review)
        for sentence in sentences:

                stn = sentence.encode('ascii', errors='ignore')
                stn2 = stn.decode()
                writer.writerow([restaurant,stn2,stars,date])
file.close()