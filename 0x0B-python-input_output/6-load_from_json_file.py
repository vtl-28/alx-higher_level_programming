#!/usr/bin/python3

'''
load_from_json_file method that creates an Object from a “JSON file”
'''
import json


def load_from_json_file(filename):
    ''' open file to be read '''
    with open(filename, 'r', encoding='utf-8') as f:
        ''' create object from read contents '''
        return json.loads(f.read())
