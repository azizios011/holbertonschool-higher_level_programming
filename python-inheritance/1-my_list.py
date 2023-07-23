#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """Class  that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)

        Args:
            list (list): legacy list

        Return:
            list sorted in ascending order
        """
        print(sorted(self))
