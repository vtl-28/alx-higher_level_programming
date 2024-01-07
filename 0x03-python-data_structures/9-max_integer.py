#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)
    for i in range(length - 1):
        if my_list[i] < my_list[i + 1]:
            my_list[i] = my_list[i]
        else:
            my_list[i + 1] = my_list[i]
    return (my_list[-1])
