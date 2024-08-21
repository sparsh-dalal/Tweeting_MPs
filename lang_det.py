import pandas as pd
df_account1 = pd.read_pickle(r'D:\SAKTHI BALAN/tweetss_500.csv')
for i in range(0,41):
    try:
        print(i,df_account1['Username'][i] ,df_account1['Content'][i][0], len(df_account1['Content'][i]) )
    except:
        print(i , 'NI')
