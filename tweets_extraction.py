import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime as dt

# Created a list to append all tweet attributes(data)

final_dates = []
final_likecount = []
final_retweetcount = []
username = []
# Using TwitterSearchScraper to scrape data and append tweets to list
file = pd.read_csv('MP_list(No of tweets).csv')
b = file['Username']
c = file['Tweets_count']
d = file['Verification Status']
for a in range(0, 2):
    print(a)
    attributes_container = []
    x = b[a]
    if d[a] != False:
        x = b[a][1:]
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"from:{x}").get_items()):
            if i > int(c[a]):
                break
            print(type(tweet.date))

            attributes_container.append([tweet.date, tweet.likeCount, tweet.retweetCount])
            # print(attributes_container)

        tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Retweet Count"])
        tweets_df['Date Created'] = tweets_df['Date Created'].dt.date
        tweets_df = tweets_df.sort_values(by=['Date Created'])
        date1 = tweets_df['Date Created'].to_list()
        likes = tweets_df['Number of Likes'].to_list()
        retweet = tweets_df['Retweet Count'].to_list()
        username.append(x)
        final_likecount.append(likes)
        final_retweetcount.append(retweet)
        final_dates.append(date1)
        tweets_df = tweets_df.drop(["Date Created", "Number of Likes", "Retweet Count"], axis='columns')
        print(final_dates)

    else:
        username.append(x)
        final_likecount.append('Null')
        final_retweetcount.append('Null')
        final_dates.append('Null')

# cutoff = dt.date(2019, 7, 1)
# sliding = []
# tweet_arr = []
# actual_tweets = []
# for i in range(len(final_dates)):
#
#     full = final_dates
#
#     count = 0
#     if d[i] != False:
#         while (cutoff >= full[i][count]):
#             count = count + 1
#
#         total = len(full[i]) - count
#         tweet_arr.append(total)
#         n = int(total / 2)
#         #print(n)
#         case1 = (full[i][count + n] - full[i][count]).days
#         for k in range(0, n):
#             if (case1 > (full[i][count + n + k] - full[i][count + k]).days):
#                 case1 = (full[i][count + n + k] - full[i][count + k]).days
#                 why = k
#         '''print(count + n + why)
#         print(count + why)
#         print(full[i][count + n + why])
#         print(full[i][count + why])'''
#         sliding.append(case1)
#         #print(sliding)
#         actual_tweets.append(len(full[i]))
#     else:
#         tweet_arr.append('0')
#         sliding.append('0')
#         actual_tweets.append('0')
#
#     if(i==540):
#       dict1 = {'Username': username, 'Date Created': final_dates, 'Likes': final_likecount, 'Retweet': final_retweetcount,
#                 'Day_Span': sliding, 'Period_Tweets': tweet_arr, 'Actual Tweets': actual_tweets}
#       s = pd.DataFrame(dict1)
#       s.to_csv('Run_Final.csv')
#       print('process completed')
#
#
#
# dict1 = {'Username': username, 'Date Created': final_dates, 'Likes': final_likecount, 'Retweet': final_retweetcount,
#                 'Day_Span': sliding, 'Period_Tweets': tweet_arr, 'Actual Tweets': actual_tweets}
# s = pd.DataFrame(dict1)
# s.to_csv('Run_Final_1.csv')
# print('Process done')