#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_dict = {}
    for i, j in a_dictionary.items():
        n_dict[i] = j * 2
    return (n_dict)
