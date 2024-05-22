#!/usr/bin/python3
"""Creates a class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
