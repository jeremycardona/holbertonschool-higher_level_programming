#!/usr/bin/python3
"""module that pickles and depickles a custom python object"""
import pickle


class CustomObject():
    """custom class fields and methods"""
    name = str()
    age = int()
    is_student = bool()

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "w") as write_file:
                pickle.dump(self, write_file)
        except Exception:
            print("Error pickling")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "r") as read_file:
                return pickle.load(read_file)
        except Exception:
            print("Error depickling")
            return None
