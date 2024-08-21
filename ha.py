import string
from collections import Counter
from nltk.corpus import stopwords
import pandas as pd


df_account1 = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\tweet_content_16march.csv')

dataf = pd.read_csv(r'C:\Users\dalal\PycharmProjects\Tweepy\MP_list(No of tweets).csv')
User = dataf['Username']
b = dataf['Party Name']

file2 = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Runining_Files\Month_Change.csv')
Month = file2['Month_Change']

STOPWORDS = set(stopwords.words('english'))
STOPWORDS_FILE = r'C:\Users\dalal\Downloads\final_stopwords.txt'
# Add stopwords from all Indian languages supported by nltk to the STOPWORDS set
with open(STOPWORDS_FILE, 'r', encoding='utf-8') as f:
    STOPWORDS |= set(f.read().splitlines())

def clean_tokenize(sentence):
    # Define custom translation table to remove punctuation except for # and @ symbols
    table = str.maketrans('', '', string.punctuation.replace('#', '').replace('@', ''))
    # Remove all punctuation except for # and @ symbols and convert to lowercase
    sentence = sentence.translate(table).lower()
    # Tokenize the sentence
    tokens = sentence.split()
    # Filter out stop words
    tokens = [token for token in tokens if token not in STOPWORDS]
    return tokens


sentences = []
# print(Month[122][34])
# print(len(df_account1['Content'][122]) - Month[122][34] + 1)
# print(len(df_account1['Content'][122]) - Month[122][35] + 1)
# print(df_account1['Content'][122][(len(df_account1['Content'][122]) - Month[122][35] + 1):(len(df_account1['Content'][122]) - Month[122][34] + 1)])
for i in range(0,542):
    if b[i] != 'Bharatiya Janata Party' and b[i] != 'Indian National Congress' and b[i]!= 'Shiv Sena':
        sentences.extend(df_account1['Content'][i][(len(df_account1['Content'][i]) - Month[i][44] + 1):(len(df_account1['Content'][i]) - Month[i][0] + 1)])
print(len(sentences))

filtered_words = []
for sentence in sentences:
    words = clean_tokenize(sentence)
    for token in words:
        if token.startswith('#'):  # filter words that start with # or @
            filtered_words.append(token)

word_counts = Counter(filtered_words)
popular_words = []
for x in word_counts:
    if word_counts[x] > 1:
        popular_words.append([x,word_counts[x]])

popular_words.sort(key= lambda x: x[1], reverse=True)
print(len(popular_words))
