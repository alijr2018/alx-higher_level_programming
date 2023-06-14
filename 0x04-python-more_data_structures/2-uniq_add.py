#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set()
    for i in my_list:
        unique_int.add(i)
    return (sum(unique_int))
