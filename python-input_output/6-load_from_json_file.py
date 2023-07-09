#!/usr/bin/python3
"""This function takes one parameter, 'filename',
which is the name of the JSON file from which
the object should be created."""


import json

"""The 'load_from_json_file' function uses the 'json'
module's 'loads' function to load the JSON string
from the file."""


def load_from_json_file(filename):

    """Inside the function, we use the 'open' function with read
    mode ("mode='r'") and UTF-8 encoding ("encoding='utf-8'")
    to open the file in a context manager."""

    with open(filename, mode='r', encoding='utf-8') as file:
        json_str = file.read()

        """We read the contents of the file using the 'read'
        method of the file object, which gives us the JSON string."""

        obj = json.loads(json_str)
        return obj
