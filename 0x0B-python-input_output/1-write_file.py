#!/usr/bin/python3

''' write_file method to write contents to a text file '''


def write_file(filename="", text=""):
    ''' open text file to write to '''
    with open(filename, 'w', encoding='utf-8') as f:
        ''' write contents to text file '''
        w = f.write(text)
        return w
