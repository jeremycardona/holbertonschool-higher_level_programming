#!/usr/bin/python3
"""module for from_json_string"""


import json


def from_json_string(my_str):
    """return an object represented by a json string"""'
    return json.loads(my_str)
