#!/usr/bin/python3

def uppercase(s):
    for chars in s:
        if 97 <= ord(chars) <= 122:
            chars = chr(ord(chars) - 32)
        print("{}".format(chars), end="")
    print("")
