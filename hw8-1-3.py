# Author: MOG 12/9/21

def in_half(string):
    length = len(string)
    half_length = length // 2

    print(string[0:half_length])
    print(string[half_length:length])

string = input("Enter your string to be cut in 2: ")

in_half(string)

in_half("racecars")
in_half("string")
in_half("nice")