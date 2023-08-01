#!/usr/bin/python3
"""
This module provides a function add_integer(a, b)

which adds two numbers together.
"""


def add_integer(a, b=98):
    """
    Adds two num (a, b) together. Both must be int or float. Returns int sum.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
