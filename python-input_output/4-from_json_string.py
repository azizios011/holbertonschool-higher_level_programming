#!/usr/bin/python3
"""This function takes one parameter, 'my_str',
which is the JSON string to be converted to a Python object."""


import json


def from_json_string(my_str):

    """Inside the function, we use the 'json.loads' function
    to parse the JSON string and convert it to a Python object."""

    return json.loads(my_str)
