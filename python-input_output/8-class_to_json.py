#!/usr/bin/python3
"""module for class_to_json"""

import json


def class_to_json(obj):
    """return the dictionary description"""
    return vars(obj)
