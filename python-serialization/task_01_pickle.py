#!/usr/bin/python3
import pickle
import os


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        for key in self.__dict__.keys():
            print(f"{key.capitalize()}: {self.__dict__[key]}")


    def serialize(self, filename: str):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """Load and return an instance of CustomObject from a file."""
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (pickle.PickleError, EOFError):
            return None
