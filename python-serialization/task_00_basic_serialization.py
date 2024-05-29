#!/usr/bin/python3
"""module for serializing and deserializing"""


import json


def serialize_and_save_to_file(data, filename):
    """ serialize data"""
    with open(filename, "w") as write_file:
        json.dump(data, write_file)

def load_and_deserialize(filename):
    """deserialize data"""
    with open(filename, "r") as read_file:
        data = json.load(read_file)
        return data
