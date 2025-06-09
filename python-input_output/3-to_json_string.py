#!/usr/bin/python3
'''create JSON string'''


import json


def to_json_string(my_obj):
    '''module JSON string'''
    json_string = json.dumps(my_obj)
    return json_string
