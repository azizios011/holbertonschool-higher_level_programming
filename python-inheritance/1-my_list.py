#!/usr/bin/python3
"""A subclass of list that can print itself sorted."""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        sorted_list = sorted(self)
        """Use the built-in sorted function to create a new sorted list"""
        print(sorted_list)
        """Print the sorted list"""
