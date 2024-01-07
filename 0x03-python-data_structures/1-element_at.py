#!/usr/bin/python3

def element_at(my_list, idx):
    length_of_list = len(my_list)

    if idx < 0:
        return (None)

    if idx > length_of_list - 1:
        return (None)

    return (my_list[idx])
