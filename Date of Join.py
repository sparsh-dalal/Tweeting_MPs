import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt

file = pd.read_csv(r'C:\Users\dalal\Downloads\Information.csv')
Date = file['Created_At']
b = file['Verification_Status']
print(type(Date[0]))

print(len(Date))
temp = []
for i in range(len(Date)):
    if b[i]!=False:
        string = Date[i]

        # define the regular expression pattern
        pattern = r"^\d{4}-\d{2}-\d{2}"

        # extract the matches using the pattern
        matches = re.findall(pattern, str(string))
        print(matches)
        # convert the matches to date strings
        dates = [datetime.strptime(match, '%Y-%m-%d').date().strftime('%Y-%m-%d') for match in matches]
        try:
            date_obj = datetime.strptime(dates[0], '%Y-%m-%d').date()
            if date_obj > datetime.strptime('2019-07-01', '%Y-%m-%d').date():
                temp.append(date_obj)
        except:
            pass

date_series = pd.Series(temp)

# Convert the Series to a pandas datetime column
date_series = pd.to_datetime(date_series, errors='coerce')

data = pd.DataFrame()
data['join_month'] = date_series.dt.month
data['join_year'] = date_series.dt.year

# Calculate the cumulative sum of people who joined each month
counts = data.groupby(['join_year', 'join_month']).size().cumsum()

# Plot the result
ax = counts.plot(kind='bar', color = 'maroon', bottom =340)
plt.xlabel('Month, Year')
plt.ylabel('Total Number of MPs on Twitter')
plt.title('Total Number of MPs on Twitter by Month, Year')

# Format the x-axis labels to show only the month and year
labels = ['{:02}-{}'.format(m, y) for y, m in counts.index]
ax.set_xticklabels(labels)

plt.show()
