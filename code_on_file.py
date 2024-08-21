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
sentences = []
#for i in range(0,542):
sentences.extend(df_account1['Content'][110])
print(len(sentences))
search_word = 'गोड्डा'
counter = 0
for sentence in sentences:
    if search_word in sentence:
        counter = counter + 1

print(counter)
# Define a function to clean and tokenize each sentence
def clean_tokenize(sentence):
    # Remove punctuation and convert to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
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



def clean_tokenize_user(sentence):
    # Remove punctuation and convert to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    # Tokenize the sentence
    tokens = sentence.split()
    # Filter out stop words
    tokens = [token for token in tokens if token not in STOPWORDS]
    list3 = list(set(tokens) & set(Tuser))
    return list3



filtered_words = []
for sentence in sentences:
    words = clean_tokenize(sentence)
    for token in words:
        if token.startswith('#'):  # filter words that start with #
            filtered_words.append(token)


list=[]
new = []
word_counts = Counter(filtered_words)
for x in word_counts:
    if word_counts[x] > 10:
        list.append([x,word_counts[x]])
        new.append(x)


list.sort(key= lambda x: x[1], reverse=True)
#for item in list:
#print(new)
print(list)
#if 'ShaheenBagh' in new:
    #print("dsj")