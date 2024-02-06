#!/usr/bin/python3

''' save_to_json_file method that writes an Object to a text file,
using a JSON representation
'''

import json


def save_to_json_file(my_obj, filename):
    ''' open text file to write to '''
    with open(filename, 'w', encoding='utf-8') as f:
        ''' write object to text file '''
        f.write(json.dumps(my_obj))
