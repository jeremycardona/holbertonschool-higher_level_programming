#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Ensure number is positive
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

output_string = f"Last digit of {number} is {last_digit} and "

if last_digit > 5:
    print(output_string + "is greater than 5")
elif last_digit == 0:
    print(output_string + "is 0")
else:
    print(output_string + "is less than 6 and not 0")
