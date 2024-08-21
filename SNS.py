import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
file= pd.read_csv('Status1.csv')
b=file['Username']
for a in range(0,1):
    x = b[a]
    if b[a]!='ERR':
        x=b[a][1:]
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{x}').get_items()):
            if i > 1000:
                break
            attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])


tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
print(tweets_df)