#!/usr/bin/python3
'''
This module provides a function that prints a square
made up of the character '#'.
'''


def print_square(size):
    '''
    Prints a square with the character '#'.
    Args:
        size (int): The length of the square's sides.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    '''
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
