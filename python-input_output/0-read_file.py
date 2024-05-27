#!/usr/bin/python3
"""Module for read_file function"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8") as file:
        fileread = file.read()
        print(fileread)