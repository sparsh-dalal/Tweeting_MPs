import pandas as pd
from datetime import datetime

file = pd.read_csv('MP_final_update.csv')
file2 = pd.read_csv('MP_list.csv')

verification_status = file2['Verification Status']
date_created = file['Date Created']

cutoff = datetime(2019, 7, 1).date()
sliding = []
tweet_arr = []
actual_tweets = []

for i in range(0, len(verification_status)):
    if verification_status[i] != False:
        date_list = eval(date_created[i])

        if len(date_list) > 0:
            # Filter tweets based on the cutoff date
            tweet_dates = [date for date in date_list if date >= cutoff]
            x = len(tweet_dates)

            # Sort the dates
            tweet_dates.sort()

            # Initialize variables
            min_successive_days = x
            start_date = tweet_dates[0]
            end_date = tweet_dates[0]
            count = 1

            # Iterate through the dates
            for i in range(1, x):
                if tweet_dates[i] > tweet_dates[i - 1]:
                    count += 1
                    end_date = tweet_dates[i]
                else:
                    if count >= x / 2:
                        min_successive_days = min(min_successive_days, count)
                        start_date = tweet_dates[i]
                        end_date = tweet_dates[i]
                        count = 1

            # Check the last sequence
            if count >= x / 2:
                min_successive_days = min(min_successive_days, count)

            # Print the result
            print("Minimum number of successive days:", min_successive_days)
            print("Start date:", start_date)
            print("End date:", end_date)
        else:
            print("No tweets found after the cutoff date")
    else:
        print("No tweets found after the cutoff date")
