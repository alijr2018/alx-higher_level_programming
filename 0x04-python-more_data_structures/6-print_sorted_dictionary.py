#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    _keys = sorted(a_dictionary.key())
    for i in _keys:
        j = a_dictionary[i]
        print(f"{i}: {j}")
