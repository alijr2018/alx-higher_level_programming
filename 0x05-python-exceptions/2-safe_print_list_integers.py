#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    loop = 0
    try:
        for j in range(x):
            if type(my_list[j]) == int:
                print("{:d}".format(my_list[j]), end="")
                loop += 1
    except IndexError:
        pass

    print("")
    return (loop)
