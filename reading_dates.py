import pandas as pd
import string
from collections import Counter
import datetime
import nltk
from nltk.corpus import stopwords
import re

df = pd.read_pickle('final_re_dates.csv')
df1 = pd.read_pickle('tweet_content_16march.csv')

nltk.download('stopwords')
nltk.download('indian')

# Define the stopword list for English
STOPWORDS = set(stopwords.words('english'))
STOPWORDS_FILE = r'C:\Users\dalal\Downloads\final_stopwords.txt'
# Add stopwords from all Indian languages supported by nltk to the STOPWORDS set
with open(STOPWORDS_FILE, 'r', encoding='utf-8') as f:
    STOPWORDS |= set(f.read().splitlines())

# define list of common words to exclude



# define function to clean and tokenize tweet text
def clean_tweet_text(tweet_text):
    # remove punctuation
    tweet_text = tweet_text.translate(str.maketrans("", "", string.punctuation))
    # convert to lowercase
    tweet_text = tweet_text.lower()
    # tokenize words
    tweet_text = re.sub(r"http\S+", "", tweet_text)
    words = tweet_text.split()
    # remove common words
    words = [word for word in words if word not in STOPWORDS]
    return words


# define function to get month from date string
def get_month_from_date(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return date_obj.strftime("%Y-%m")


# initialize dictionary to store word frequency for each person
person_word_freq = {}

# initialize dictionary to store overall word frequency
overall_word_freq = Counter()

# loop through list of tweets
for tweet in tweet_list:
    # extract tweet data
    user = tweet["user"]
    text = tweet["text"]
    date_str = tweet["date"]
    # clean and tokenize tweet text
    words = clean_tweet_text(text)
    # get month from date string
    month = get_month_from_date(date_str)
    # update person_word_freq dictionary
    if user not in person_word_freq:
        person_word_freq[user] = {}
    if month not in person_word_freq[user]:
        person_word_freq[user][month] = Counter()
    person_word_freq[user][month].update(words)
    # update overall_word_freq dictionary
    overall_word_freq.update(words)

# print word frequency for each person per month
for user in person_word_freq:
    print(f"Word frequency for {user}:")
    for month in person_word_freq[user]:
        print(f"\t{month}:")
        for word, count in person_word_freq[user][month].most_common():
            print(f"\t\t{word}: {count}")

# print overall word frequency
print("Overall word frequency:")
for word, count in overall_word_freq.most_common():
    print(f"\t{word}: {count}")

print(df['Dates'][33][0])
print(df1['Content'][33][-1])