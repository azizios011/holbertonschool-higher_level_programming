#!/usr/bin/python3
"""the implementation of the 'pascal_triangle' function"""


def pascal_triangle(n):

    """The function starts by checking if 'n' is less
    than or equal to 0. In such cases, it returns
    an empty list."""

    if n <= 0:
        return []

    """If 'n' is greater than 0, it initializes 'triangle'
    with the first row '[1]'."""

    triangle = [[1]]

    """Then, it uses two nested loops to generate subsequent rows."""

    for i in range(1, n):
        row = [1]
        """The outer loop runs from 1 to 'n-1'."""
        for j in range(1, i):

            """and the inner loop runs from 1 to 'i-1'."""

            num = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(num)

        """ Within the inner loop, the value of each element is
        computed by adding the two elements from the previous row."""

        row.append(1)

        """The current row is then appended to the 'triangle' list."""

        triangle.append(row)

    """Finally, the function returns the 'triangle'
    list representing Pascal's triangle."""

    return triangle
