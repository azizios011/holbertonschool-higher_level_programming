#!/usr/bin/python3
'''
This module provides a function that prints a name in the format:
My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
    Prints a full name in the following format:
    My name is <first name> <last name>

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed

    Raises:
        TypeError: If either first_name or last_name is not a string.
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
