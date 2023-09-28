#!/usr/bin/python3
"""interview,a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """this function it's role is founding te bigger number among the other"""
    if not list_of_integers:
        return None
    value = list_of_integers[0]

    for i in list_of_integers[1:]:
        if i > value:
            value = i
    return (value)
