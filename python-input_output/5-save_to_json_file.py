#!/usr/bin/python3
"""This function takes two parameters: 'my_obj',
which is the object to be saved as JSON, and 'filename',
which is the name of the file to which
the JSON should be written."""


import json


def save_to_json_file(my_obj, filename):

    """Inside the function, we use the 'open' function with
    write mode ("mode='w'") and UTF-8 encoding ("encoding='utf-8'")
    to open the file in a context manager."""

    with open(filename, mode='w', encoding='utf-8') as file:

        """We convert the 'my_obj' object to a JSON string using
        the 'to_json_string' function,"""

        json_str = json.dumps(my_obj)

        """Then, we use the 'write' method of the file object
        to write the JSON string to the file."""

        file.write(json_str)
