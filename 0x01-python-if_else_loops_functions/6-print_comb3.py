#!/usr/bin/python3
for i in range(10):
    for n in range(i + 1, 10):
        print("{:d}{:d}".format(i, n), end=", " if i != 8 or n != 9 else "\n")
