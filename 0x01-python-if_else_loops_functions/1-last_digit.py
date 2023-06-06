#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
_s = str(number)
if int(_s[-1:]) < 6:
    print(f"Last digit of {number:d} is {_s[-1]} and is less than 6 and not 0")
if int(_s[-1:]) == 0:
    print(f"Last digit of {number:d} is {_s[-1:]} and is 0")
if int(_s[-1:]) > 5:
    print(f"Last digit of {number:d} is {_s[-1:]} and is greater than 5")
