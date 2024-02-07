#!/usr/bin/py<F7>thon3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
