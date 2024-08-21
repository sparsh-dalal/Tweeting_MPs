import pandas as pd
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.corpus import indian
#nltk.download('punkt')
# Download stopwords if needed
# nltk.download('stopwords')
# nltk.download('indian')

# Define the stopword list for English
STOPWORDS = set(stopwords.words('english'))
STOPWORDS_FILE = r'C:\Users\dalal\Downloads\final_stopwords.txt'
# Add stopwords from all Indian languages supported by nltk to the STOPWORDS set
with open(STOPWORDS_FILE, 'r', encoding='utf-8') as f:
    STOPWORDS |= set(f.read().splitlines())

dataf = pd.read_csv(r'C:\Users\dalal\PycharmProjects\Tweepy\MP_list(No of tweets).csv')
User = dataf['Username']

file2 = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Runining_Files\Month_Change.csv')
Month = file2['Month_Change']

# load the pickled DataFrame file for account1
df_account1 = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\tweet_content_16march.csv')

# print the first 5 rows of the DataFrame
#print(df_account1['Content'][65])


# Download stopwords if needed
# import nltk
# nltk.download('stopwords')

# Define the stopword list


# Define a list of sentences to analyze

# Define a function to clean and tokenize each sentence
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

# Use a Counter object to count the frequency of each word


# Iterate over each sentence, clean and tokenize it, and add its words to the Counter object
Tuser = []
for username in User:
    words = clean_tokenize(username)
    for token in words:
        Tuser.append(token)

Tuser1 = []
for j,username in enumerate(User):
    if dataf['Party Name'][j] == 'Dravida Munnetra Kazhagam':
        words = clean_tokenize(username)
        for token in words:
            Tuser1.append(token)


import string

def clean_tokenize_user(sentence, Tuser):
    # Remove punctuation and convert to lowercase
    table = str.maketrans('', '', string.punctuation.replace('#', '').replace('@', ''))
    # Remove all punctuation except for # and @ symbols and convert to lowercase
    sentence = sentence.translate(table).lower()
    # Tokenize the sentence
    tokens = sentence.split()
    # Filter out stop words and words that do not start with "@" or are in Tuser
    tokens = [token for token in tokens if token not in STOPWORDS and token.startswith('@') and token in Tuser and token not in Tuser1]
    #tokens = [token for token in tokens if token not in STOPWORDS and token.startswith('@') and token not in Tuser]
    return tokens


final_append = []
final_append2 = []
sentences = []
for i in range(0,542):
    if dataf['Party Name'][i] == 'Dravida Munnetra Kazhagam':
        sentences.extend(df_account1['Content'][i][0:(len(df_account1['Content'][i]) - Month[i][0] + 1)])

print(len(sentences))
sum = 0
wow = []
for x in range(0,1):
    filtered_words = []
    for sentence in sentences:
        words = clean_tokenize_user(sentence,Tuser)
        for token in words:
            wow.append(sentence)
            filtered_words.append(token)


    word_counts = Counter(filtered_words)
    popular_words = []
    for x in word_counts:
        if word_counts[x] > 1:
            popular_words.append([x, word_counts[x]])
            sum = sum + word_counts[x]

    popular_words.sort(key=lambda x: x[1], reverse=True)

print(sum)
print(popular_words)
#print(wow)






