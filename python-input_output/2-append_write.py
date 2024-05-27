#!/usr/bin/python3
"""Module for append_write function"""


def append_write(filename="", text=""):
    """append write function"""
    with open(filename, mode='a', encoding="utf-8") as file:
        return file.write(text)
