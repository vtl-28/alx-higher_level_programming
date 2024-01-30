#!/usr/bin/python3

'''
This is the "4-print_square" module.
The 4-print_square module supplies one function, def print_square(size).
'''


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
