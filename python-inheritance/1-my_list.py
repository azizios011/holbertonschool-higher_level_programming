#!/usr/bin/python3
"""define class Mylist that inherite from class list"""


class MyList(list):
    """define fields and metod of my class"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
