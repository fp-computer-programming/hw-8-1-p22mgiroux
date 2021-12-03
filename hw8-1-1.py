# Author: MOG 12/3/21

def anagram_check(word1,word2):
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()

    if list1 == list2:
        print("{} and {} are anagrams.".format(word1, word2))
    else:
        print("{} and {} are not anagrams.".format(word1, word2))

first = input("What is your first word? ")
second = input("What is your second word? ")

anagram_check(first,second)

anagram_check("Damon Albarn","Dan Abnormal")
anagram_check("working hard","hardly working")
anagram_check("cat","dog")