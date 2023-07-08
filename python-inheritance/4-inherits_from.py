#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """ checks if the type of obj is a subclass of a_class.
    This condition will be True if obj is an instance of a class that directly
    or indirectly inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
