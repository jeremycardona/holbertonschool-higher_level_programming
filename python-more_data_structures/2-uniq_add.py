#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    result = 0

    for n in my_list:
        if n not in uniq:
            result += n
            uniq.add(n)
    return uniq
