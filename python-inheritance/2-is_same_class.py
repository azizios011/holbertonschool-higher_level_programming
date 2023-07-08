#!/usr/bin/python3
"""defie a methode is_same_class"""


def is_same_class(obj, a_class):
    """returns true if object is an instance of the given class """
    return type(obj) is a_class
