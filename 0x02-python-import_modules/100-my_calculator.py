#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    _operator = sys.argv[2]
    b = int(sys.argv[3])

    sol = None
    if _operator == '+':
        sol = add(a, b)
    elif _operator == '-':
        sol = sub(a, b)
    elif _operator == '*':
        sol = mul(a, b)
    elif _operator == '/':
        sol = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {_operator} {b} = {sol}")
    sys.exit(0)
