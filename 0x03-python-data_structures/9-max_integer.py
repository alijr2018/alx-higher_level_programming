#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return (None)
    value = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > value:
            value = my_list[i]
        i += 1
    return (value)