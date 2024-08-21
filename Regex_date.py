import pandas as pd
import re
from datetime import date

file = pd.read_csv(r'C:\Users\dalal\Downloads\Final_Collection.csv')
b = file['Date Created']

print(len(b))
temp=[]
for i in range(len(b)):
    string = b[i]

    # define the regular expression pattern
    pattern = r"datetime\.date\((\d{4}),\s*(\d{1,2}),\s*(\d{1,2})\)"

    # extract the matches using the pattern
    matches = re.findall(pattern, str(string))

    # convert the matches to date objects
    dates = []
    for match in matches:
        year, month, day = map(int, match)
        date_obj = date(year, month, day)
        dates.append(date_obj)
    temp.append(dates)


file = file.assign(Dates = temp)
file = file.drop(columns=['Date Created'],axis=1)
file.to_pickle("final_re_dates.csv")
