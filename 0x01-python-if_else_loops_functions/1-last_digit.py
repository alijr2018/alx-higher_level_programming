#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
_s = str(number)
if number < 0:
    _l = '-' + _s[-1:]
else:
    _l = _s[-1:]

_l = int(_l)
if _l < 6 and _l != 0:
    print(f"Last digit of {number:d} is {_l} and is less than 6 and not 0")
if _l == 0:
    print(f"Last digit of {number:d} is 0 and is 0")
if _l > 5:
    print(f"Last digit of {number:d} is {_l} and is greater than 5")
