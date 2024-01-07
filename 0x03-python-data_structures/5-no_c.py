#!/usr/bin/env python3

# convert string to list
# check if string is empty
# get length of list
# loop through list
# check if any element is equal to C or C
# if so, add empty space at that index
# join the altered array to create a string again

def no_c(my_string):
    converted_str = list(my_string)
    length_of_list = len(converted_str)

    if my_string == " ":
        pass
    for i in range(length_of_list):
        if converted_str[i] == 'c' or converted_str[i] == 'C':
            converted_str[i] = ""

    return ("".join(converted_str))
