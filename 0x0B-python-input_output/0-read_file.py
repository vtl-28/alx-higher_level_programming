#!/usr/bin/python3

''' read_file method to read contents of text file '''


def read_file(filename=""):
    ''' read contents of text file '''
    with open(filename, encoding="utf-8") as f:
        print(f.read())
