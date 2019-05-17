
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.



Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.


Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database



Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""
from  selenium import webdriver
import pandas as pd
from pymongo import MongoClient
import sqlite3
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("M:/forsk/chromedriver_win32/chromedriver.exe")
browser.get(url)
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
connection1=sqlite3.connect('new3.db')
cur=connection1.cursor()
cur.execute("""CREATE TABLE table1(
        BID_NO TEXT,
        items TEXT,
        Quantity TEXT,
        Department TEXT,
        Start TEXT,
        End TEXT
        )""")
df222.columns = ["Bid No","items","Quantity required","Department Name And Address","Start Date/Time","End Date/Time"]
for i in range(5):
    cur.execute("INSERT INTO table1 VALUES ('"+LBID_NO[i]+"','"+Litems[i]+"','"+LQuantity[i]+"','"+LDepartment[i]+"','"+LStart[i]+"','"+LEnd[i]+"')")
#cur.execute("INSERT INTO table1 VALUES ('Bid No','items','Quantity required','Department Name And Address','Start Date/Time','End Date/Time')")
cur.execute("SELECT * FROM table1")
df222 = pd.DataFrame(cur.fetchall())



"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 3306
MySQL database name:  databasenamedata
MySQL username: ravisuthar
MySQL user password: 7425967157
Email address:  udaan.ravi@gmail.com
MYSQL URL : mysql://yourusername:dbpassword@db4free.net/yourdbname

"""


from  selenium import webdriver
import pandas as pd
import mysql.connector
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("M:/forsk/chromedriver_win32/chromedriver.exe")
browser.get(url)
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

connection1=mysql.connector.connect(user='ravisuthar', password='7425967157',
                              host='db4free.net', database = 'databasenamedata')
cur=connection1.cursor()

cur.execute("""CREATE TABLE table1(
        BID_NO TEXT,
        items TEXT,
        Quantity TEXT,
        Department TEXT,
        Start TEXT,
        End TEXT
        )""")

for i in range(5):
    cur.execute("INSERT INTO table1 VALUES ('"+LBID_NO[i]+"','"+Litems[i]+"','"+LQuantity[i]+"','"+LDepartment[i]+"','"+LStart[i]+"','"+LEnd[i]+"')")
#cur.execute("INSERT INTO table1 VALUES ('Bid No','items','Quantity required','Department Name And Address','Start Date/Time','End Date/Time')")
cur.execute("SELECT * FROM table1")
df333 = pd.DataFrame(cur.fetchall())
df333.columns = ["Bid No","items","Quantity required","Department Name And Address","Start Date/Time","End Date/Time"]
















