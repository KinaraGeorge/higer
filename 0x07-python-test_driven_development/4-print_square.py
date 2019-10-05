#!/usr/bin/python3
"""

A function to print a square

"""

def print_square(size):
    """Print a square made of #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    stra = '#' * size
    for x in range(size):
        print(stra)
