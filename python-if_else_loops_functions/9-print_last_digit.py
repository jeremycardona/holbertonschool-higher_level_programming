#!/usr/bin/python3

def print_last_digit(number):
    last_digit = int()
    if (number < 0):
        last_digit = number * -1
    last_digit = last_digit % 10
    print(last_digit)
    return last_digit
