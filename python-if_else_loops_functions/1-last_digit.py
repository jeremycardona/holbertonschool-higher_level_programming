#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= 1

print(number)
if number % 10 > 5:
    print(f"The last digit of {number} is {number % 10} and greater than 5")
elif number % 10 == 0:
    print(f"The last digit of {number} is {number % 10} and is 0")
elif number % 10 < 6:
    print(f"The last digit {number} is {number % 10} and is less than 6 and not 0")
