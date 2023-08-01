#!/usr/bin/python3
'''
This module provides a function `text_indentation` for manipulating
text strings
'''


def text_indentation(text):
    '''
    This function prints a text with two new lines after each of these
    characters: ., ? and :
    Args:
        text (str): The text to process. Must be a string
    Raises:
        TypeError: If `text` is not a string.
    '''
    if type(text) != str:
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in (characters):
            result += "\n\n"
    split_line = result.split("\n")
    for i in range(len(split_line)):
        if i == len(split_line) - 1:
            print(split_line[i].strip(), end="")
        else:
            print(split_line[i].strip())
