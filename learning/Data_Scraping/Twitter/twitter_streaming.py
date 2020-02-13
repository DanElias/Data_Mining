
# mount google drive
from google.colab import drive
drive.mount('/content/drive')

path = '/content/drive/My Drive/BT4222/twitter_streaming_data'

import os
from datetime import datetime
import json
import random
import re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = '<access_token>'
access_token_secret = '<access_token_secret>'
consumer_key = '<consumer_key>'
consumer_secret = '<consumer_key_secret>'

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, json_data):
        # print(json_data)
        filename = re.sub(r'\s|\/|:', r'_', '%s.txt' % str(datetime.now()))
        # fileloc = './twitter_stream_data/' + filename
        fileloc = os.path.join(path, filename)
  
        # 1% chance of printing out the file location
        if random.randint(0, 100) == 0:
            print(fileloc)
        # End of if statement.
            
        with open(fileloc, 'w') as f:
            f.write(json_data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['obama', 'trump', 'clinton'])

"""
Note that this is a while loop! It runs until the cows come home!
To terminate this infinite loop, press the stop button in the iPython notebook's TOOLBAR.

You will see a "KeyboardInterrupt" error message -- which is what you are supposed to get.
"""