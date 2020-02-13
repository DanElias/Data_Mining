import tweepy
from tweepy import OAuthHandler

access_token = '<access_token>'
access_token_secret = '<access_token_secret>'
consumer_key = '<consumer_key>'
consumer_secret = '<consumer_key_secret>'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.search(q='obama', count=50, lang='en')

# Convert a result to JSON with "._json"
print(type(results[0]))
print(type(results[0]._json))

list_of_status_dicts = []

for result in results:
    list_of_status_dicts.append( result._json )

# This code is the same as the code in the cell above, just that it's shorter.
# [Python list comprehension] Convert all the results into a `list of dictionaries`
##list_of_status_dicts = [result._json for result in results]

len(list_of_status_dicts)
list_of_status_dicts[0].keys()
list_of_status_dicts[0]['text']

query = 'trump'
max_tweets = 555

searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=query, lang='en', count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # Depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break

len(searched_tweets)

# Convert all the results into a `list of dictionaries`
list_of_status_dicts_2 = [x._json for x in searched_tweets]

len(list_of_status_dicts_2)

list_of_status_dicts_2[0]['text']