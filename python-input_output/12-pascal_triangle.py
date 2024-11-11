#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of height n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        List[List[int]]: Pascal's triangle as a list of lists of integers.
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    triangle = []

    # Generate each row of the Pascal's triangle
    for i in range(n):
        row = [None] * (i + 1)  # Create a row with None placeholders
        row[0], row[-1] = 1, 1  # First and last elements are always 1

        # Fill in the interior elements
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle
