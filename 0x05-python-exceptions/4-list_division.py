#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    s = []
    for j in range(list_length):
        try:
            if j < len(my_list_1)
            else 0
            if j < len(my_list_2)
            else 0

            if isinstance(my_list_1[i], (int, float))
            and isinstance(my_list_2[i], (int, float)):
                try:
                    d_s = my_list_1[i] / my_list_2[i]
                except ZeroDivisionError:
                    print("division by 0")
                    d_s = 0
                s.append(d_s)
            else:
                print("wrong type")
                s.append(0)
        except IndexError:
            print("out of range")
            s.append(0)
    return (s)
