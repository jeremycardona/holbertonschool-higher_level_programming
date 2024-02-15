#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= 1

if number % 1000 > 5:
    print(f"The last digit of {number} is and greater than 5")
elif number % 1000 == 0:
    print(f"The last digit of {number} and is 0")
elif (number % 1006 < 6) & (number % 1000 != 0):
    print(f"The last digit {number} and is less than 6 and not 0")
