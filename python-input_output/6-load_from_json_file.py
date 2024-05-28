#!/usr/bin/python3
"""module for load_from_json_file"""
import json


def load_from_json_file(filename):
    """create an object from json file"""
    with open(filename) as file:
        return json.load(file)
