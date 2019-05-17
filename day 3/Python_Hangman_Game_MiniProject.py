# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""
import random
print("enter atleast two values ")
list2=list()
while True:
    list1=input(">")
    if not list1:
        break
    list2.append(list1)
correct=random.choice(list2)
guess=""
guessno=int((len(list2))/2)
flag=0

while(guess != correct and guessno > 0 ):
    print("You have to guess one from the following")
    print("note you have only {} options ".format(guessno))
    print(list2)
    guess=input(">")   
    if(guess in list2):
        print("Your Choice is : ",guess)
    else:
        print("Wrong choice ......enter the correct statement")
    if(guess is correct):
        print("You got the right one...................you won")
        exit
    list2.remove(guess)
    guessno -= 1    
if(guessno is 0):
    print("you lose due to more bad attempts")


"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

"""
Challenge 3
Read the words from a file

"""

"""
Challenge 4
    Get the list of Internet after web scrapping
"""
