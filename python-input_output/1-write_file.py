#!/usr/bin/python3
"""Module for write_file function"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
