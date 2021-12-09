# Author: MOG 12/9/21



def sort_str(my_string):
    my_list = list(my_string)
    sorted_list = my_list.copy()
    sorted_list.sort()

    if sorted_list == my_list:
        print("This list is sorted.")
    else:
        print("This list is not sorted.")

my_string = input("Please input a list of numbers or letters not seperated by anything: ")
sort_str(my_string)

sort_str("jklmno")
sort_str("aAaAa")
sort_str("$#!@")