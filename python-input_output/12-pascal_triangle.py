#!/usr/bin/python3
""" a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of height n
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    triangle = []

    """Generate each row of the Pascal's triangle"""
    for i in range(n):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1

        # Fill in the interior elements
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle
