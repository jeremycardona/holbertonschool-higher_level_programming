#!/usr/bin/python3
"""Creates a class that defines a student"""


class Student:
    """Class with attributes and method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        student_dict = vars(self)
        data = {}
        if isinstance(attrs, list):
            for key in attrs:
                if isinstance(key, str) and key in student_dict:
                    data[key] = student_dict[key]
            return data
        return student_dict
