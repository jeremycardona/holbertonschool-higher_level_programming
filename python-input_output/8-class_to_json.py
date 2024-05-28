#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """return the dictionary description"""
    return vars(obj)
