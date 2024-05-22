def lookup(obj):
    """
    This function returns the list of available attributes and methods of an object.
    
    Parameters:
    obj (any): The object whose attributes and methods are to be listed.

    Returns:
    list: A list of strings, each representing an attribute or method of the object.
    """
    return dir(obj)
