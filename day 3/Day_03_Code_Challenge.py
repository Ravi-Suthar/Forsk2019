
"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
value=input("Enter the numbers : ")
value=value.split(",")
print("list : ",value)
tup=tuple(value)
print("tuple :",tup)

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    (Monday, Wednesday, Thursday, Saturday)
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
value=input("Enter the numbers : ")
value=value.split(",")
print(value)
list1=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(list1)
for x in range(len(list1)):
    if(value[x] is list1[x]):
        pass
    else:
        value.insert(x,list1[x])
print(value)
"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
"""


dict1=dict()
while True:
    user_input = input("Enter goods and price >")   
    if not user_input:
        break
    user_input=user_input.split()
    if(user_input[0] not in dict1.keys()):
        dict1[user_input[0]]=int(user_input[1])
    else:
        var=dict1[user_input[0]]
        dict1[user_input[0]]=var+int(user_input[1])
print(dict1)
    
     
"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
def fix_teen(n):
    if(n==15 or n==16):
        return(n)
    elif(n in range(13,20)):
        return 0
    else:
        return n
    
dict1=dict()
while True:
    user_input = input("Enter key and value >")   
    if not user_input:
        break
    user_input=user_input.split()
    dict1[user_input[0]]=int(user_input[1])
print(dict1)
sum=0
for x in dict1.values():
    var=fix_teen(x)
    sum=sum+var
print(sum)

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

string1=input("enter the string :").lower()
dict1=dict()
for x in string1 :
    if(x in dict1.keys()):
        dict1[x]=dict1[x]+1        
    else:
        dict1[x]=1
print(dict1)

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
string1=input("enter the string :").lower()
string2="abcdefghijklmnopqrstuvwxyz"
counter2=0
string3="0123456789"
counter3=0
for ele in string1:
    if(ele in string2):
        counter2=counter2+1
    elif(ele in string3):
        counter3=counter3+1
print("Letters :",counter2)
print("Digits :",counter3)

"""
Two words are anagrams if you can rearrange the letters of one to spell the second.  
For example, the following words are anagrams:

 ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']

Hint: How can you tell quickly if two words are anagrams?  
Dictionaries allow you to find a key quickly.  

"""
string1=input("enter the string 1 :").lower()
string2=input("enter the string 2 :").lower()
set1=set(string1)
set2=set(string2)
s3=set1.union(set2)
if(s3 is set1):
    print("Words are anagram")
    exit
else:
    print("words are not anagram")


"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""

s1 = {1,2,3,4,5}
print ("Set1 :",s1)
s2 = {3,4,5,6,7}
print ("Set 2 ",s1)
s4 = s1.intersection(s2) 
print("Final Intersection set is :",s4)
"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""
list1=[12,24,35,24,88,120,155,88,120,155]
for x in range(len(list1)):
    for y in range(x+1,len(list1)):
        if(list1[x] is list1[y]):
            del list1[y]
print(list1)


"""
Code Challenge
  Name: 
    Mailing List
  Filename: 
    mailing.py
  Problem Statement:
  I recently decided to move a popular community  mailing list (3,000 subscribers, 
  60-80 postings/day) from my server to Google Groups. 
  I asked people to joint he Google-based list themselves, 
  and added many others myself, as the list manager. 
  However, after nearly a week, only half of the list had been moved. 
  I somehow needed to learn which people on the old list hadn't yet 
l  signed up for the new list.


  Fortunately, Google will let you export a list of members of a group to 
  CSV format. 
  Also, Mailman (the list-management program I was using on
  my server) allows you to list all of the e-mail addresses being used 
  for a list. Comparing these lists, I think, offers a nice chance to look
  at several different aspects of Python, and to consider how we can 
  solve this real-world problem in a "Pythonic" way.


  The goal of this project is thus to find all of the e-mail addresses on 
  the old list that aren't on the new list. The old list is in a file 
  containing one e-mail address per line, as in:
    
  Hint:
      Refer to mailing.txt for the new and old list of email addresses.
      
"""
