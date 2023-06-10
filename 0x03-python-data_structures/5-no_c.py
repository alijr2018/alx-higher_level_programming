#!/usr/bin/python3
def no_c(my_string):
    string = ""
    i = 0
    while i < len(my_string):
        char = my_string[i]
        if char != 'c' and char != 'C':
            string += char
        i += 1
        return (string)
