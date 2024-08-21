from bs4 import BeautifulSoup
import selenium
import requests as rqst
import webbrowser as wb
import numpy as np
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

import re

from selenium.webdriver.common.keys import Keys
from time import sleep

import config

'''auth = tweepy.OAuthHandler(config.API_KEY, config.ACCESS_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)'''

url = rqst.get('https://loksabhaph.nic.in/Members/AlphabeticalList.aspx')
testpage = url.text
soup = BeautifulSoup(testpage, 'lxml')
data = []
table1 = soup.find('table', id='ContentPlaceHolder1_tblMember')
headers = []
for i in table1.find_all('thead'):
    abc = i.find_all('td')
    for q in abc:
        title = q.text
        a = title.replace("\n", "")
        b = a.replace("\r", "")
        headers.append(b)
mydata = pd.DataFrame(columns=headers)
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    rows = []
    for p in row_data:
        row = p.text
        rows.append(row)
    length = len(mydata)
    mydata.loc[length] = rows
mydata.to_csv('list.csv', index=False)
final = pd.read_csv("list.csv")
final = pd.read_csv('list.csv', header=0, usecols=["                                                        Name Of Member                                                    "])
names = final['                                                        Name Of Member                                                    '].tolist()


names.remove(names[0])

Member_Name = []

for i in names:
    new = i.replace('  ','')
    new2 = new.replace('\n','')
    new3 = new2.replace('\r','')
    Member_Name.append(new3)


final1 = pd.read_csv('list.csv',header=0,usecols=["                                                        Party Name                                                    "])
party = final1['                                                        Party Name                                                    '].tolist()


party.remove(party[0])

Party_name = []

for i in party:
    new20 = i.replace('  ','')
    new22 = new20.replace('\n','')
    new23 = new22.replace('\r','')
    Party_name.append(new23)

final2 = pd.read_csv('list.csv',header=0,usecols=["                                                        Constituency (State)                                                    "])
state = final2['                                                        Constituency (State)                                                    '].tolist()


state.remove(state[0])

Constituency = []
State_Name = []
Caste = []

for i in state:
    new10 = i.replace('  ','')
    new12 = new10.replace('\n','')
    new14 = new12.replace(')','')
    new13 = new14.replace('\r','')
    if new13.count('(')==2:
        finarr = new13.split("(")
        Constituency.append(finarr[0])
        State_Name.append(finarr[2])
        Caste.append(finarr[1])
    else:
        finarr1 = new13.split("(")
        Constituency.append(finarr1[0])
        State_Name.append(finarr1[1])
        Caste.append("General")

#print(Member_Name)
PATH="C:\Program Files\Drivers\chromedriver-win64\chromedriver.exe"
display_name=[]
Verifictaion=[]
a3=[]
a4=[]
a5=[]
a6=[]
i=0
for c in Member_Name:

    driver = webdriver.Chrome(PATH)  # open the chrome

    driver.get("https://www.google.com/")  # put the url of the website u want to open
    # driver.maximize_window() # For maximizing window
    print(i)
    i = i+1

    sleep(2)

    # print(driver.title)

    # driver.quit()

    # driver.maximize_window()

    # driver.set_window_size(width,height)

    username = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

    username.send_keys(c + " twitter account")
    sleep(2)
    username.send_keys(Keys.ENTER)
    sleep(3)
    first_link = driver.find_element(By.TAG_NAME, 'h3')

    first_link.click()
    sleep(5)
    try:
        username = driver.find_element(By.XPATH,
                                   '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span')
    except:
        display_name.append('ERR')

    else:
        display_name.append(username.text)
    sleep(2)
    try:
        verified = driver.find_element(By.XPATH,
                                       '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span[2]/div')
    except:
        #print("does not exist")
        Verifictaion.append("False")
    else:
        #print("It exists")
        Verifictaion.append("True")
    '''joining= driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/span/span')
    print(joining[0].text)
    #a3.append(joining[-1].text)

    following= driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div[2]/a/span[1]/span')
    print(following.text)
    a4.append(following.text)

    followers= driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div[1]/a/span[1]/span')
    print(followers.text)
    a5.append(followers.text)

    total_tweets= driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div')
    a6.append(total_tweets.text)
    driver.close()

writer = pd.ExcelWriter('pandas_multiple.xlsx',engine ='xlsxwriter')
df = pd.DataFrame()

df['USERNAME']=a1
df['VERIFICATION']=a2
df['date of joining']=a3
df['FOLLOWING']=a4
df['FOLLOWERS']=a5
df['TOTAL TWEETS']=a6
print(df)'''

dict1 = {'Name of Member': Member_Name, 'Party Name': Party_name, 'Constituency': Constituency,'State':State_Name,'Caste':Caste,'Username': display_name, 'Verification Status': Verifictaion}
database = pd.DataFrame(dict1)
database.to_csv('Status1.csv')
