#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list_copy = my_list[:]

    for i in range(len(list_copy) - 1):
        if list_copy[i] == search:
            list_copy[i] = replace

    return (list_copy)
