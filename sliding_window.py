import pandas as pd
import numpy as np
import datetime

#file = pd.read_csv('Status1.csv')
#date_tweeted = file['Date_created']
cutoff = datetime.date(2022, 12, 16)
sliding = []
for i in range(0, 1):
    #full = date_tweeted[i]
    full = [[datetime.date(2018, 1, 17), datetime.date(2018, 1, 17), datetime.date(2018, 1, 26), datetime.date(2018, 3, 6), datetime.date(2018, 3, 20), datetime.date(2018, 9, 8), datetime.date(2018, 9, 8), datetime.date(2018, 10, 22), datetime.date(2018, 10, 25), datetime.date(2018, 11, 10), datetime.date(2018, 11, 15), datetime.date(2019, 1, 12), datetime.date(2019, 3, 28), datetime.date(2019, 3, 28), datetime.date(2019, 3, 30), datetime.date(2019, 4, 2), datetime.date(2019, 4, 2), datetime.date(2019, 4, 2), datetime.date(2019, 4, 2), datetime.date(2019, 4, 2), datetime.date(2019, 4, 5), datetime.date(2019, 4, 6), datetime.date(2019, 4, 6), datetime.date(2019, 4, 6), datetime.date(2019, 4, 7), datetime.date(2019, 4, 7), datetime.date(2019, 4, 7), datetime.date(2019, 4, 7), datetime.date(2019, 4, 14), datetime.date(2019, 4, 14), datetime.date(2019, 4, 16), datetime.date(2019, 4, 18), datetime.date(2019, 6, 27), datetime.date(2019, 6, 28), datetime.date(2019, 7, 6), datetime.date(2019, 12, 11), datetime.date(2019, 12, 12), datetime.date(2019, 12, 15), datetime.date(2019, 12, 24), datetime.date(2020, 1, 14), datetime.date(2020, 3, 13), datetime.date(2020, 3, 27), datetime.date(2020, 5, 27), datetime.date(2020, 6, 10), datetime.date(2020, 7, 13), datetime.date(2020, 8, 2), datetime.date(2020, 9, 9), datetime.date(2020, 9, 10), datetime.date(2020, 12, 4), datetime.date(2020, 12, 5), datetime.date(2020, 12, 9), datetime.date(2021, 3, 29), datetime.date(2021, 4, 17), datetime.date(2021, 6, 5), datetime.date(2021, 6, 19), datetime.date(2021, 7, 10), datetime.date(2021, 8, 25), datetime.date(2021, 8, 27), datetime.date(2021, 10, 13), datetime.date(2021, 10, 13), datetime.date(2021, 12, 4), datetime.date(2021, 12, 4), datetime.date(2021, 12, 4), datetime.date(2021, 12, 4), datetime.date(2021, 12, 6), datetime.date(2021, 12, 6), datetime.date(2021, 12, 8), datetime.date(2021, 12, 10), datetime.date(2022, 1, 16), datetime.date(2022, 2, 17), datetime.date(2022, 2, 22), datetime.date(2022, 3, 28), datetime.date(2022, 3, 31), datetime.date(2022, 4, 14), datetime.date(2022, 4, 16), datetime.date(2022, 5, 7), datetime.date(2022, 5, 19), datetime.date(2022, 5, 19), datetime.date(2022, 5, 19), datetime.date(2022, 5, 28), datetime.date(2022, 6, 10), datetime.date(2022, 6, 24), datetime.date(2022, 6, 27), datetime.date(2022, 6, 27), datetime.date(2022, 6, 30), datetime.date(2022, 7, 3), datetime.date(2022, 7, 3), datetime.date(2022, 7, 9), datetime.date(2022, 7, 10), datetime.date(2022, 7, 11), datetime.date(2022, 8, 3), datetime.date(2022, 8, 3), datetime.date(2022, 8, 7), datetime.date(2022, 8, 17), datetime.date(2022, 8, 24), datetime.date(2022, 8, 29), datetime.date(2022, 9, 3), datetime.date(2022, 9, 12), datetime.date(2022, 9, 13), datetime.date(2022, 9, 13), datetime.date(2022, 9, 19), datetime.date(2022, 9, 21), datetime.date(2022, 9, 22), datetime.date(2022, 9, 24), datetime.date(2022, 9, 27), datetime.date(2022, 9, 29), datetime.date(2022, 10, 2), datetime.date(2022, 10, 4), datetime.date(2022, 10, 6), datetime.date(2022, 10, 7), datetime.date(2022, 10, 9), datetime.date(2022, 10, 13), datetime.date(2022, 10, 15), datetime.date(2022, 10, 15), datetime.date(2022, 10, 15), datetime.date(2022, 10, 15), datetime.date(2022, 10, 15), datetime.date(2022, 10, 16), datetime.date(2022, 10, 16), datetime.date(2022, 10, 16), datetime.date(2022, 10, 16), datetime.date(2022, 10, 16), datetime.date(2022, 10, 16), datetime.date(2022, 10, 16), datetime.date(2022, 10, 17), datetime.date(2022, 10, 18), datetime.date(2022, 10, 18), datetime.date(2022, 10, 18), datetime.date(2022, 10, 23), datetime.date(2022, 10, 25), datetime.date(2022, 10, 25), datetime.date(2022, 10, 25), datetime.date(2022, 10, 28), datetime.date(2022, 10, 29), datetime.date(2022, 11, 2), datetime.date(2022, 11, 2), datetime.date(2022, 11, 3), datetime.date(2022, 11, 5), datetime.date(2022, 11, 5), datetime.date(2022, 11, 5), datetime.date(2022, 11, 5), datetime.date(2022, 11, 8), datetime.date(2022, 11, 8), datetime.date(2022, 11, 8), datetime.date(2022, 11, 8), datetime.date(2022, 11, 9), datetime.date(2022, 11, 9), datetime.date(2022, 11, 9), datetime.date(2022, 11, 9), datetime.date(2022, 11, 13), datetime.date(2022, 11, 19), datetime.date(2022, 11, 19), datetime.date(2022, 11, 21), datetime.date(2022, 11, 23), datetime.date(2022, 11, 23), datetime.date(2022, 11, 29), datetime.date(2022, 12, 6), datetime.date(2022, 12, 9), datetime.date(2022, 12, 10), datetime.date(2022, 12, 10), datetime.date(2022, 12, 10), datetime.date(2022, 12, 10), datetime.date(2022, 12, 14), datetime.date(2022, 12, 14), datetime.date(2022, 12, 14), datetime.date(2022, 12, 15), datetime.date(2022, 12, 15), datetime.date(2022, 12, 15), datetime.date(2022, 12, 16), datetime.date(2022, 12, 16), datetime.date(2022, 12, 18), datetime.date(2022, 12, 18), datetime.date(2022, 12, 25), datetime.date(2022, 12, 28), datetime.date(2022, 12, 29), datetime.date(2022, 12, 31)]]
    count = 0
    while(cutoff>=full[0][count]):
        count = count + 1
    print(len(full[0]))
    total = len(full[0]) - count
    print(total)
    n = int(total/2)
    print(n)
    case1 = (full[0][count +n] -  full[0][count]).days
    for k in range(0,n):
        if (case1 > (full[0][count + n + k] - full[0][count+ k]).days):
            case1 = (full[0][count + n + k] - full[0][count+k]).days
    print(count + n + k)
    print(count+k)
    print(full[0][count + n + k])
    print(full[0][count+k])
    sliding.append(case1)
    print(sliding)

