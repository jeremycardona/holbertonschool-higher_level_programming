#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# the output should be:
# the last digit of number, followed by
# if the last digit is greater than 5: "and is is greater than 5"
# if the last digit is 0: the string "and is 0"
# if the last difit is less than 6 and not 0: the string
# "and is lesss than 6 and not 0
# followed by a newline

# convert negative randoms here
if number < 0:
    number *= 1

if number % 1000 > 5:
    print(f"The last digit of {number} is and greater than 5")
elif number % 1000 == 0:
    print(f"The last digit of {number} and is 0")
elif (number % 1006 < 6) & (number % 1000 != 0):
    print(f"The last digit {number} and is less than 6 and not 0")
