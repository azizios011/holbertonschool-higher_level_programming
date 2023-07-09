#!/usr/bin/python3
""" the 'to_json_string' implementation. """


import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON string representation.

    Args:
        my_obj (object): The Python object to be converted.

    Returns:
        str: The JSON string representation of the object.
    """
    json_string = json.dumps(my_obj)

    """ Use the json.dumps() function to convert the object to JSON string."""

    """Return the JSON string."""

    return json_string
