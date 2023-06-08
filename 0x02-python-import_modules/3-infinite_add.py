#!/usr/bin/python3
import sys


if __name__ == "__main__":
    i = sys.argv[1:]
    j = sum(int(arg) for arg in i)
    print(j)