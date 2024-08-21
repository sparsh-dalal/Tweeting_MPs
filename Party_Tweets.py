import pandas as pd

df_account1 = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\tweet_content_16march.csv')

dataf = pd.read_csv(r'C:\Users\dalal\PycharmProjects\Tweepy\MP_list(No of tweets).csv')
User = dataf['Username']

file2 = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Runining_Files\Month_Change.csv')
Month = file2['Month_Change']
number = []
bjp = []
for j in range(0,43):
    sentences = []
    for i in range(0,542):
        if dataf['Party Name'][i]!='Shiv Sena' and dataf['Party Name'][i]!='Bharatiya Janata Party' and dataf['Party Name'][i]!='All India Trinamool Congress' and dataf['Party Name'][i]!='Indian National Congress' and dataf['Party Name'][i]!='Dravida Munnetra Kazhagam' and dataf['Party Name'][i]!='Yuvajana Sramika Rythu Congress Party' and dataf['Party Name'][i]!='Nationalist Congress Party':
        #if dataf['Party Name'][i]=='Nationalist Congress Party':
            sentences.extend(df_account1['Content'][i][(len(df_account1['Content'][i]) - Month[i][j+1] + 1):(len(df_account1['Content'][i]) - Month[i][j] + 1)])
    number.append(j)
    bjp.append(len(sentences))


print(number,bjp)

file = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Runining_Files\Party_Tweet.csv')

file['Others'] = bjp

file.to_pickle('Party_Tweet.csv')
