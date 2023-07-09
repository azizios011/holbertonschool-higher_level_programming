#!/usr/bin/python3
"""the 'append_write' function that appends a string
to the end of a text file and returns the number
of characters added"""


def append_write(filename="", text=""):

    """This function takes two parameters: 'filename',
    which specifies the name of the file to which the string
    should be appended, and 'text', which is the string
    to be appended to the file."""

    with open(filename, mode='a', encoding='utf-8') as file:

        """The function uses the 'with' statement to open
        the file in a context manager. It opens the file
        in append mode ("mode='a'") and specifies
        the UTF-8 encoding("encoding='utf-8'")."""

        return file.write(text)
