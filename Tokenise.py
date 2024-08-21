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



def clean_tokenize_user(sentence):
    # Remove punctuation and convert to lowercase
    table = str.maketrans('', '', string.punctuation.replace('#', '').replace('@', ''))
    # Remove all punctuation except for # and @ symbols and convert to lowercase
    sentence = sentence.translate(table).lower()
    # Tokenize the sentence
    tokens = sentence.split()
    # Filter out stop words
    tokens = [token for token in tokens if token not in STOPWORDS]
    list3 = list(set(tokens) & set(Tuser))
    return list3

final_append = []
final_append2 = []
for i in range(0,542):
    sentences =[]
    sentences = df_account1['Content'][i][0:(len(df_account1['Content'][i]) - Month[i][0] + 1)]
    print(len(sentences))
    filtered_words = []
    for sentence in sentences:
        words = clean_tokenize_user(sentence)
        for token in words:
            filtered_words.append(token)

    list1=[]
    list2 = []
    word_counts = Counter(filtered_words)
    for x in word_counts:
        if word_counts[x] > 1:
            list1.extend([x])
            for i in range(word_counts[x]):
                list2.extend([x])


    #list1.sort(key= lambda x: x[1], reverse=True)

    final_append.append(list1)
    final_append2.append(list2)



df_2 = pd.DataFrame()


df_2['Username'] = User
df_2['Name of Member'] = dataf['Name of Member']
df_2['Tags_Unique'] = final_append
df_2['Tags_Repeat'] = final_append2
df_2.to_pickle('Revised_Tags_Harshit.csv')