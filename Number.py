import datetime
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_pickle('Start_End.csv')

start = file['Start Date']
end = file['End Date']

start_date = datetime.date(2019, 7, 1)
end_date = datetime.date(2023, 2, 1)
delta = datetime.timedelta(days=31)

dates_list = []

while start_date <= end_date:
    dates_list.append(start_date)
    new_month = start_date.month % 12 + 1
    if new_month == 1:
        new_year = start_date.year + 1
    else:
        new_year = start_date.year
    start_date = start_date.replace(month=new_month, year=new_year, day=1)



group = []

for i in range(len(dates_list)-1):
    count = 0
    for j in range(0, 542):
        if start[j] is not None and end[j] is not None and start[j] <= dates_list[i + 1] and end[j] >= dates_list[i]:
            count += 1

    group.append(count)

for i in range(len(group)):
    print(dates_list[i].strftime('%B %Y'), group[i])
print(len(dates_list),len(group))

fig= plt.figure(figsize=(10,5))
plt.bar(dates_list[0:43], group,width=15)



plt.xlabel("Time")
plt.ylabel('Active MPs')
plt.title('Active MPs per month')

# show plot
plt.show()



