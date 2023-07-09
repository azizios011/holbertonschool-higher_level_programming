#!/usr/bin/python3
"""the 'write_file' function that writes a string to a text
file and returns the number of characters written"""


def write_file(filename="", text=""):

    """This function takes two parameters: 'filename',
    which specifies the name of the file to be written, and 'text',
    which is the string to be written to the file."""

    with open(filename, mode='w', encoding='utf-8') as file:

        """The function uses the 'with' statement to open the file
        in a context manager. It opens the file in write mode ('mode='w'')
        and specifies the UTF-8 encoding ('encoding='utf-8'')."""

        return file.write(text)
