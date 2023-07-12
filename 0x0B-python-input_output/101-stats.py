#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics.
"""

import sys

lines_read = 0
total_file_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        lines_read += 1
        ip, _, _, _, status_code, file_size = line.strip().split(' ')

        total_file_size += int(file_size)

        if status_code not in status_codes:
            status_codes[status_code] = 0
        status_codes[status_code] += 1

        if lines_read % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_codes.keys()):
                print("{}: {}".format(code, status_codes[code]))
            print()

except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))
