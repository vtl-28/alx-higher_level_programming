#!/usr/bin/python3

# loop through list
# check for 2, if found, replace it with 89

def search_replace(my_list, search, replace):
    list_copy = my_list[:]

    if len(list_copy) < 1:
        return (None)

    for i in range(len(list_copy) - 1):
        if list_copy[i] == search:
            list_copy[i] = replace

    return (list_copy)
