#!/usr/bin/python3
""" base class model """

class Base:

    __nb_objects = 0
    def __init__(self, id=None):
        if (id is not None):
            id = id
        else:
            __nb_objects += 1
            id = id
