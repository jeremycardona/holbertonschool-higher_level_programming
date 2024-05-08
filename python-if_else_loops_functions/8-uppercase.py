#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
        print("{}".format(upper_char), end="")
    print("")
