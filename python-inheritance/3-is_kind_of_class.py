#!/usr/bin/python3
"""is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """return True if it is an instance of any class
    that is a subclass of a_class otherwise, it will return False."""
    return isinstance(obj, a_class)
