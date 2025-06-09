#!/usr/bin/python3
'''student class to json'''


class Student:
    '''student class to json'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
