"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""

import json
json_string="""
[
{
"Profession":"Student",
"First Name":"Ravi",
"Last Name":"Suthar",
"Photo"="www.google.com";
"Department":"CSE",
"Research Areas":["ML","IOT"],
"Contact Details": 1234567890 
},
{
"Profession":"Faculty",
"First Name":"Ravis",
"Last Name":"Suthar",
"Photo"="ww.google.com";
"Department":"CSE",
"Research Areas":["ML","IOT"],
"Contact Details":1234567890
}
]
"""

with open("data1.json","w") as f1:
    json.dump(json_string,f1)

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests
from datetime import datetime
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3
response = requests.get(url)
print(response.content)
jsondata = response.json()
print (jsondata)
print("Longitude and Latitude : ",jsondata['coord']['lon']," and ",jsondata['coord']['lat'])
print("Weather Condition : ",jsondata['weather'][0]['main'])
print("Wind speed :",jsondata['wind']['speed'])
print("Sun Rise Time : ",datetime.fromtimestamp(jsondata['sys']['sunrise']).strftime('%H:%M:%S')," AM")
print("Sun Set Time : ",datetime.fromtimestamp(jsondata['sys']['sunset']).strftime('%H:%M:%S'), " PM")

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests
url=""
response1 = requests.get(url)
print(response1.content)
jsondata1 = response1.json()
float1=float(input("Enter the INR value: "))
print("Value : ",float1*jsondata1['USD_PHP'])


# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com







