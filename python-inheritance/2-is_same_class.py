#!/usr/bin/python3
"""
    Function that returns if the object is exacly
    an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
        Return true if the object is exacly an instance
        of the specified class
    """
    return type(obj) is a_class
