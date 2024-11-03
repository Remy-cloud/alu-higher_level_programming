#!/usr/bin/python3
"""Defines a class Square that represents a square with size,
position, and printing capabilities.
"""


class Square:
    """Represents a square with private size and position attributes,
    including getters, setters, and methods for area calculation and display.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a given size and position,
        with type and value validation.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, ensuring it is a
        non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square, ensuring it is a tuple of
         2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#', with the specified position.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print new lines for position[1] (vertical offset)
        for _ in range(self.__position[1]):
            print("")

        # Print each line of the square with position[0] spaces
        # (horizontal offset)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
