#!/usr/bin/python3
"""creating a class rectangle """


class Rectangle:
    """a class that define the rectangle"""
    # public class attributes
    number_of_instances = 0
    print_symbol = "!"

    def __init__(self, width=0, height=0):
        """initialize the rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """calculate the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """return a string representation of the rectangle
        using the '#' character."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                          for _ in range(self.height)])

    def __repr__(self):
        """return a string representation of the rectangle
         for reproduction. """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print a message when instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
