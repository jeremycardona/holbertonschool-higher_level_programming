#!/usr/bin/python3
""" base class model """

class Base:

    __nb_objects = 0
    def __init__(self, id=None):
        if (not id):
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
