#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file,
after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
    """def of append_after"""
    lines = []

    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)
