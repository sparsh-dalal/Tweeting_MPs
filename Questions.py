import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns


file= pd.read_csv('Status1.csv')


file.rename(columns={'Party Name':'Party_Name','Name of Member':'Name_of_member','Verification Status':'verification_status'}, inplace=True)

#print(file.head())
'''x=file.groupby('Party_Name').Party_Name.count()
print(type(x))
x.plot(style='.')

plt.show()'''
'''z=file.groupby('verification_status').verification_status.value_counts()
print(z)'''
y=file[['Party_Name','verification_status','Username']]
x=file.groupby('Party_Name').Party_Name.count()
print(x)
y1= y.loc[y['verification_status']==True]
y11=sum(y1.groupby('Party_Name').value_counts())/5.43
print(y11)
y2=y.loc[y['verification_status']==False]

y22=sum(y2.groupby('Party_Name').value_counts())/5.43

print(y22)

z=y.loc[y['Username']=='ERR']

z11=sum(z.groupby('Party_Name').value_counts())/5.43
print(z11)


#print(file.Name_of_member.describe())

#print(file.Caste.value_counts())

#print(file.groupby(['Caste']).mean())

#print(file.groupby(['Caste','verification_status']).value_counts())