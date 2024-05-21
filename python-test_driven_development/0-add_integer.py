#!/usr/bin/python3
"""
    Sum of two integers
"""


def add_integer(a, b=98):
    """
        Check that the two variables are integers or floats
        then convert to int and return the sum
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
