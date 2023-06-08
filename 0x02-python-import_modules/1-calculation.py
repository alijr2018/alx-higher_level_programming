#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    r_a = add(a, b)
    r_s = sub(a, b)
    r_m = mul(a, b)
    r_d = div(a, b)
    print(f"{a} + {b} =", r_a)
    print(f"{a} - {b} =", r_s)
    print(f"{a} * {b} =", r_m)
    print(f"{a} / {b} =", r_d)