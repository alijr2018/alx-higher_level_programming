#!/usr/bin/python3
def uppercase(str):
    u_s = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            u_s += chr(ord(c) - (ord('a') - ord('A')))
        else:
            u_s += c
    print(u_s)
