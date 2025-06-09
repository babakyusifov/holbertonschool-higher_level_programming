#!/usr/bin/python3
'''About from json string to object'''
import json


def from_json_string(my_str):
    '''Modul from json str to obj'''
    json_obj = json.loads(my_str)
    return json_obj
