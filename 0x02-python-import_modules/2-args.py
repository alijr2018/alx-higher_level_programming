#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    n = len(argv)

    if n == 0:
        print("0 arguments.")
    else:
        print(f"{n} argument{'s' if n != 1 else ''}:")
        j = 1
        while j <= n:
            arg = argv[j-1]
            print(f"{j}: {arg}")
            j += 1
