#!/usr/bin/python3

''' to_json_string method that returns JSON representation of an object '''

import json


def to_json_string(my_obj):
    ''' serialize object '''
    return json.dumps(my_obj)
