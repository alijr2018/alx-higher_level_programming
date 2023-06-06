#!/usr/bin/python3
import sys
i = ord('a')
while i <= ord('z'):
    sys.stderr.write(chr(i))
    i += 1
