#!/usr/bin/python3
def uppercase(str):
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
