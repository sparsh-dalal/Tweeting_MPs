import bisect
import datetime
import pandas as pd

df = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\final_re_dates.csv')


#print(df['Dates'][0])

start_date = datetime.date(2019, 7, 1)
end_date = datetime.date.today()

ind = []
for i in range(0,542):
    index_list = []
    dates_list = df['Dates'][i]
    current_month = start_date
    while current_month <= end_date:
        try:
            index = dates_list.index(current_month)
        except ValueError:
            index = bisect.bisect_left(dates_list, current_month)
        index_list.append(index)
        current_month = current_month.replace(day=1) + datetime.timedelta(days=32)
        current_month = current_month.replace(day=1)
    ind.append(index_list)
    #print(index_list)
print(ind[110])
