#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length_of_items = len(my_list)
    copy_of_list = my_list[:]

    if idx < 0 or idx > length_of_items - 1:
        return (my_list)

    copy_of_list[idx] = element
    return (copy_of_list)
