#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    sol = []
    for i in my_list:
        sol.append(i % 2 == 0)
    return (sol)
