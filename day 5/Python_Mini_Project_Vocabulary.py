

"""
Code Challenge
  Name: 
    Vocabulary
  Filename: 
    Vocabulary.py
  Problem Statement:
    Novel = james_joyce_ulysses.txt
    The claim is that James Joyce used in his novel more words than any other author. 
    Actually his vocabulary is above and beyond all other authors, 
    maybe even Shakespeare.
    
    1. Find the total number of words in the novel
    2. many words occur multiple time:["the", "while", "good", "bad", "ireland", "irish"]
    3. Quality of a novel is the number of different words.
       Find the number of different words used
    4. look at the other novels and find the total words and unique words for comparison
       novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']

    5. Special Words in Ulysses novel by comparing with others, 
       words which are only used in Ulysses, store it in a file

    6. Common Words - Find the words which occur in every book.

  Hint: 
     Use Sets, Regex, File Handling
     re.findall(r"\b[\w-]+\b", ulysses_txt)
     

"""
import re
def list_of_words(filename):
    with open(filename) as f1:
        list3=list()
        list1=f1.readlines()
        for a in list1:
            list2=a.split(" ")
            for b in list2:
                list3.append(b.lower())
        for a in range(len(list3)):
            str1=""
            for b in list3[a]:
                if(b.isalpha()):
                    str1=str1+b
                else:
                    pass
                list3[a]=str1
        while ("" in list3):
            list3.remove("")
        return(list3)
        
def total_number_of_words(list1):
    return(len(list1))
    
def list_of_unique_words(list1):
    list2=list(set(list1))
    return list2
    
def dict_of_unique_words(list1):
    dict1=dict()
    for each in list1:
        if each in dict1:
            var=dict1[each]
            dict1[each]=var+1
        else:
            dict1[each] = 1
    return(dict1)
    
print("Enter the number of your choice")
print("\t\t1. Find the total number of words in the novel")
print("\t\t2. the words occur then twice")
print("\t\t3. number of unique words used")
print("\t\t4. comaprison with other novel and display common words")
print("\t\t5. comaprison with any other novel and display special words used")
            
choice = input(">>>>")
if choice is '1' :
    fname = input("Enter the name of file : ")
    list4=list_of_words(fname)
    count=total_number_of_words(list4)
    print("Total number of words are ",count)
    
if choice is '2' :
    fname = input("Enter the name of file : ")
    list1=list_of_words(fname)
    dict1=dict_of_unique_words(list1)
    for each in dict1:
        print(each," : ",dict1[each])
  
if choice is '3' :
    fname = input("Enter the name of file : ")
    list1=list_of_words(fname)
    list2=list_of_unique_words(list1)
    count=total_number_of_words(list2)
    print("Total number of unique words are ",count)
    
if choice is '4' : 
    input1=int(input("enter the number of Files you want compare : "))
    input1 -= 1
    fname = input("Enter the name of file : ")
    list1=list_of_words(fname)
    list2=list_of_unique_words(list1)
    set1=set(list2)
    for x in range(input1):
        aname = input("Enter the name of file you have to compare with : ")
        list3=list_of_words(aname)
        list4=list_of_unique_words(list3)
        set2=set(list4)
        set1=set1.intersection(set2)
    print(set1)
       
if choice is '5' :
    fname = input("Enter the name of file : ")
    list1=list_of_words(fname)
    list2=list_of_unique_words(list1)
    aname = input("Enter the name of file you have to compare with : ")
    list3=list_of_words(aname)
    list4=list_of_unique_words(list3)
    set1=set(list2)
    set2=set(list4)
    set3=set1.difference(set2)
    print("\nSpecial Words in ",fname," are ",set3)
    