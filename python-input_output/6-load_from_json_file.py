#!/usr/bin/python3
'''load from json file'''
import json


def load_from_json_file(filename):
    '''load from json file'''
    with open(filename, "r", encoding="utf-8") as file:
        my_obj = json.load(file)
        return my_obj
