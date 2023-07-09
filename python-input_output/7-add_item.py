#!/usr/bin/python3
""" the '7-add_item.py' script that adds all arguments
to a Python list and saves them to a file using JSON
representation."""


import sys
from os.path import exists
from json import load, dump

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""The script first checks if the file '"add_item.json"' exists.
If it does, it loads the existing list from the file using
the 'load_from_json_file' function. If the file doesn't exist,
it initializes an empty list."""

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

"""Next, it extends the list with the command-line arguments
'sys.argv[1:]', which represent all the arguments passed to
the script except for the script name itself."""

my_list.extend(sys.argv[1:])

"""Finally, it saves the updated list to the file using
the 'save_to_json_file' function."""

save_to_json_file(my_list, filename)
