#!/usr/bin/python3
"""

A function to print a square

"""

def print_square(size):

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    str = '#' * size
    for x in range(size):
        print(str)
