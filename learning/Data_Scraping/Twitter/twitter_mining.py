import re

def word_in_text(word, text):
    if word and text:
        word = word.lower()
        text = text.lower()
        match = re.search(word, text)
        if match:
            return True
    return False

tweets['obama'] = tweets['text'].apply(lambda tweet: word_in_text('obama', tweet))
tweets['trump'] = tweets['text'].apply(lambda tweet: word_in_text('trump', tweet))
tweets['clinton'] = tweets['text'].apply(lambda tweet: word_in_text('clinton', tweet))

tweets.head()

print(tweets['obama'].value_counts()[True])
print(tweets['trump'].value_counts()[True])
print(tweets['clinton'].value_counts()[True])

politicians = ['obama', 'trump', 'clinton']
tweets_by_politicians = [tweets['obama'].value_counts()[True], tweets['trump'].value_counts()[True], tweets['clinton'].value_counts()[True]]

x_pos = list(range(len(politicians)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_politicians, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Obama vs. Trump vs. Clinton', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(politicians)
plt.grid()