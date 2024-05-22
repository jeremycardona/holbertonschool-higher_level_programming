#!/usr/bin/python3

def lookup(obj):
    """
    This function returns the list of available attributes and methods of an object.
    
    Parameters:
    obj (any): The object whose attributes and methods are to be listed.

    Returns:
    list: A list of strings, each representing an attribute or method of the object.
    """
    if obj:
        return list(dir(obj))
    else:
        return None
