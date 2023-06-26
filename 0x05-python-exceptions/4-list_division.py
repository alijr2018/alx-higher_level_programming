#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 1

            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                raise TypeError("wrong type")

            division = dividend / divisor

            if divisor == 0:
                raise ZeroDivisionError("division by 0")

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except TypeError:
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        else:
            result.append(division)

    return (result)
