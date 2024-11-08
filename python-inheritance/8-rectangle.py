#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
""" class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """rectangle that inherits from BaseGeometry"""
    def __int__(self, width, height):
        """initialize rectangle instances"""

        self.integer_validator("width, width")
        self.__width = width

        self.integer_validator("height, height")
        self.__height = height
