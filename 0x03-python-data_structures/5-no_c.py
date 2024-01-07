#!/usr/bin/env python3

def no_c(my_string):
    converted_str = my_string[:]
    length_of_list = len(my_string)

    v = 0

    for i in range(length_of_list):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            converted_str = new_string[:(i - v)] + my_string[(i + 1):]
            v += 1

    return (converted_str)
