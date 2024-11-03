#!/usr/bin/python3

"""a square class with private instance attributes
"""


class Square:

    """give class attributes"""
    def __init__(self, size=0):
        """raising errors"""
        if not type(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """initialization"""
        self.__size = size
