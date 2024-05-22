#!/usr/bin/bash
"""Module containing inherits_from function"""


def inherits_from(obj, a_class):
    """
    This function checks if an object
    is an instance of a class that inherited
    (directly or indirectly)
    from the specified class.

    Parameters:
    obj (any): The object to be checked.
    a_class (type): The class to be checked against.

    Returns:
    bool: True if obj is an instance of a class that
    inherited from a_class; otherwise False.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
