import glob
# list_of_files = (glob.glob("./twitter_stream_data/*.txt"))
list_of_files = (glob.glob("/content/drive/My Drive/BT4222/twitter_data/*txt"))
len(list_of_files)

# Read all the TXT files into a "list of dictionary objects" called "tweets_data"

tweets_data = []

for fname in list_of_files:
    tweets_file = open(fname, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

len(tweets_data)
tweets_data[0]['text']

import pandas as pd
tweets = pd.DataFrame()

tweets['text'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'] if 'lang' in tweet else None, tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if ('place' in tweet and (tweet['place'] != None)) else None, tweets_data))

tweets.tail(10)
tweets[  tweets['country'].notnull()  ].head()

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
