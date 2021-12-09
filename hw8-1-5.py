# Author: MOG 12/9/21

def palindrome_check(word):
    if word == word[:: -1]:
        print("The word " + word + " is a palindrome because " + word + " spelled backwards is " + word[:: -1] + ".")
    else:
        print("The word " + word + " is not a palindrome because " + word + " spelled backwards is " + word[:: -1] + ".")

word = input("What is your word? ")
palindrome_check(word)

palindrome_check("racecar")
palindrome_check("monkey")
palindrome_check("dad")
