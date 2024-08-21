import pandas as pd
import csv

file= pd.read_csv('MP_list(No of tweets).csv')
b = file['Username']
c = file['Tweets_count']
d = file['Verification Status']
sum = 0
for a in range(0, 101):
    print(a)
    attributes_container = []
    x = b[a]
    if d[a] != False:
        sum = sum + int(c[a])

print(sum)