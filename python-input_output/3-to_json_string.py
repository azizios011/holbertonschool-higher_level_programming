#!/usr/bin/python3
"""This function takes one parameter, 'my_obj',
which is the object (string) to be converted to JSON."""


def to_json_string(my_obj):

    """Inside the function, we first check if the 'my_obj'
    is an instance of a string using the 'isinstance' function."""

    if isinstance(my_obj, str):

        """ If it is a string, we wrap it in double quotes
        and escape any double quotes within the string
        by replacing them with '\"'."""

        return '"' + my_obj.replace('"', '\\"') + '"'

    """If the 'my_obj' is not a string, we raise a 'TypeError'
    with a descriptive message indicating that the object
    is not JSON serializable."""

    else:
        raise TypeError
    ("{} is not JSON serializable".format(type(my_obj).__name__))
