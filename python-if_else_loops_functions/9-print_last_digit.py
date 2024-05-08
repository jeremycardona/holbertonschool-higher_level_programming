#!/usr/bin/python3

def print_last_digit(number):
    last_digit = int()
    if (number < 0):
        last_digit = number % -10
    else:
        last_digit = number % 10
    return last_digit
 
p = print_last_digit(96)
print(p)
