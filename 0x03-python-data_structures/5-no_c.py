#!/usr/bin/python3
def no_c(my_string):
    string = ""
    i = 0
    while i < len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            string += my_string[i]
        i += 1
        return (string)
