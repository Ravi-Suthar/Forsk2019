

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
link="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(link).text
soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table')
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        B.append(cells[0].text.strip())
        C.append(cells[1].text.strip())
        D.append(cells[2].text.strip())
        E.append(cells[3].text.strip())
        F.append(cells[4].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["Position","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")


"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
import pandas as pd
from collections import OrderedDict
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("M:/forsk/chromedriver_win32/chromedriver.exe")
browser.get(url)
"""
sleep(2)
for i in range(2,6):
    get_school_result = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    get_school_result.click()
    sleep(3)
sleep(5)
"""
LBID_NO=list()
Litems=list()
LQuantity=list()
LDepartment=list()
LStart=list()
LEnd=list()
for i in range(1,6):
    BID_NO=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    LBID_NO.append(BID_NO.text)
    items=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    Litems.append(items.text)
    Quantity=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span')
    LQuantity.append(Quantity.text)
    Department=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    LDepartment.append(Department.text)
    Start=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span')
    LStart.append(Start.text)
    End=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span')
    LEnd.append(End.text)
col_name = ["Bid No","items","Quantity required","Department Name And Address","Start Date/Time","End Date/Time"]
col_data = OrderedDict(zip(col_name,[LBID_NO,Litems,LQuantity,LDepartment,LStart,LEnd]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")


"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image

2
"""
from PIL import Image 
import io
import requests
import urllib
from selenium import webdriver
url = "http://forsk.in/images/Forsk_logo_bw.png"
img=requests.get(url)
a=Image



