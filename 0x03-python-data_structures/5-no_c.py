#!/usr/bin/env python3

def no_c(my_string):
    converted_str = list(my_string)
    length_of_list = len(converted_str)

    if my_string == " ":
        pass

    for i in range(length_of_list):
        if converted_str[i] == 'c' or converted_str[i] == 'C':
            converted_str[i] = ""

    return ("".join(converted_str))
