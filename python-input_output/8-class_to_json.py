#!/usr/bin/python3
"""The function 'class_to_json' takes an object 'obj'
as input and returns a dictionary
representation of the object."""


def class_to_json(obj):

    """It achieves this by accessing the '__dict__' attribute
    of the object, which contains all the instance variables
    and their corresponding values."""

    json_dict = obj.__dict__
    return json_dict
