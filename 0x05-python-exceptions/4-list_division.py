#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    s = []
    for j in range(list_length):
        try:
            if j < len(my_list_1):
                e1 = my_list_1[i]
                if j < len(my_list_2):
                    e2 = my_list_2[i]
                    if e2 != 0:
                        div = e1 / e2
                    else:
                        print("division by 0")
                else:
                    print("out of range")
            else:
                print("out of range")
                s.append(0)
        except TypeError:
            print("wrong type")
        finally:
            pass
    return (s)
