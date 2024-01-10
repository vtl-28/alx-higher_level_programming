#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()

    for keys in list(new_dir.keys()):
        new_dir[keys] *= 2
        
    return (new_dir)
