def extract_link(text):
    try:
        regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        match = re.search(regex, text)
        if match:
            return match.group()
        return ''
    except:
        return ''

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
tweets.head()
tweets.shape

tweets_with_link = tweets[ tweets['link'] != ''].copy()
tweets_with_link.head(3)
tweets_with_link.shape

print(tweets_with_link[tweets_with_link['obama']   == True]['link'])
print(tweets_with_link[tweets_with_link['trump']   == True]['link'])
print(tweets_with_link[tweets_with_link['clinton'] == True]['link'])

# Now say we want to read one of the links above, https://t.co/oua32nXu8W

# Read the HTML source of the URL: https://t.co/oua32nXu8W
import urllib.request
url = 'https://t.co/oua32nXu8W'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()
try:
    html = html.decode('utf-8')
except:
    html = html.decode('unicode_escape')

# Import BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# See the title of the HTML document

soup.title

# Extract all the paragraphs (p) and print out the content

for paragraph in soup.find_all('p'):
    if paragraph.string is not None:
        print(paragraph.string)

