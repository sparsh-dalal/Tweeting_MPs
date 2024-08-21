import pandas as pd
import datetime as dt

# Load the dates data
dates = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\final_re_dates.csv')

# Load the MP data
file = pd.read_csv(r'C:\Users\dalal\PycharmProjects\Tweepy\MP_list(No of tweets).csv')

# Extract the necessary columns
b = file['Username']
c = file['Party Name']
d = file['Verification Status']
final_dates = dates['Dates']

# Set the cutoff date
cutoff = dt.date(2019, 7, 1)

# Initialize lists to store the results
sliding = []
tweet_arr = []
actual_tweets = []
focus_start = []
focus_end = []

# Loop through each MP's tweet dates
for i in range(len(final_dates)):
    # Extract the full date range for the MP
    full = final_dates[i]

    # Check if the MP is verified
    if d[i] != False:
        # Count the number of tweets before the cutoff date
        count = 0
        while (cutoff >= full[count]):
            count = count + 1

        # Calculate the total number of tweets from the cutoff date to the last tweet date
        total = len(full) - count

        # Append the total number of tweets to the tweet_arr list
        tweet_arr.append(total)

        # Calculate the number of tweets to focus on
        n = int(total / 2)

        # Initialize variables to store the minimum number of days and the index where it occurred
        min_days = None
        min_index = None

        # Loop through all possible sliding windows of size n
        for k in range(total - n):
            # Calculate the number of days between the first and last tweet in the sliding window
            days = (full[count + k + n - 1] - full[count + k]).days

            # Check if this is the new minimum number of days
            if min_days is None or days < min_days:
                min_days = days
                min_index = k

        # Append the minimum number of days to the sliding list
        sliding.append(min_days)

        # Append the total number of actual tweets to the actual_tweets list
        actual_tweets.append(total)

        # Calculate the start and end dates of the focus period
        start_date = full[count + min_index]
        end_date = full[count + min_index + n - 1]

        # Append the start and end dates to the focus_start and focus_end lists
        focus_start.append(start_date)
        focus_end.append(end_date)

        # Print the results for this MP
        if min_days>600:
           print(f"MP: {b[i]}, Party: {c[i]}, Period Tweets: {total}, Day Span: {min_days}, Start Date: {start_date}, End Date: {end_date}")

    else:
        # If MP is not verified or has no tweets, append 0 to lists
        sliding.append(0)

        actual_tweets.append(0)
        focus_start.append(None)
        focus_end.append(None)

# # Create a dictionary and convert to DataFrame
# dict1 = {'Username': b, 'Day_Span': sliding, 'Party Name': c, 'Period_Tweets': actual_tweets, 'Start Date': focus_start, 'End Date': focus_end}
# df = pd.DataFrame(dict1)
#
# # Save DataFrame to file
# df.to_pickle('Start_End.csv')
#
# print('Process done')
