import pandas as pd

df = pd.read_pickle('Month_Change.csv')
b = df['Tweets_Monthwise']
print(df['Tweets_Monthwise'][504][34])
check = 0
month = 0
top =[]
for i in range(0,43):
    sum = 0
    for j in range(0,542):
        sum = sum + b[j][i]
    print(sum)
    top.append(sum)
    if sum > check:
        month = i
        check = sum
    elif sum == check:
        print(i)



# Get the indices of the top 5 numbers
top_indices = sorted(range(len(top)), key=lambda i: top[i], reverse=True)[:10]

print(top_indices)
