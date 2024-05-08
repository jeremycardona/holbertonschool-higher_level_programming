#!/usr/bin/python3

def print_last_digit(number):
    last_digit = int()
    if (number < 0):
        last_digit = number * -1
    print(last_digit % 10)
 
