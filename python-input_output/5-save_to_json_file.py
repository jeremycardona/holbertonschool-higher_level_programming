#!/usr/bin/python3
"""module for save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using json"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
