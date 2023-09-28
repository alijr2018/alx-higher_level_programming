#!/usr/bin/python3
#interview

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    value = list_of_integers[0]

    for i in list_of_integers[1:]:
        if i > value:
            value = i
    return (value)
