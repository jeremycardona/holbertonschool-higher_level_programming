#!/usr/bin/python3

def no_c(my_string):
    for c in my_string:
         if my_string[c] == 'c':
            del my_string[c]
     return my_string

