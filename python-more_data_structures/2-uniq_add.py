#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for my_list in set(my_list):
        result += set(my_list)
    return result
