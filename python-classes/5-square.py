#!/usr/bin/python3
"""Create a class that defines a square"""


class Square:
    """Class that represents a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size
    """setter method"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
