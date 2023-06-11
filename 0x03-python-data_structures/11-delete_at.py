#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    l_list = len(my_list)
    if idx < 0 or idx >= l_list - 1:
        return (my_list)
    else:
        del my_list[idx]
    return (my_list)
