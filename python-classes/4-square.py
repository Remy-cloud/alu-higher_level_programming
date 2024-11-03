#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)

"""


class Square:
    """Represents a square with a private size attribute,
     including getter and setter."""
    def __init__(self, size=0):
        self.size = size
        """Retrieves the size of the square"""

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            """raise"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            return self.__size ** 2
