#!/usr/bin/python3

''' append_write method to append contents to a text file '''


def append_write(filename="", text=""):
    ''' append contents to a text file '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
