#!/usr/bin/python3
"""creation of class that inherits from list"""


class Myclass(list):
    """ subclass of list with an additional method to print the list sorted"""

    def print_sorted(self):
        """prints out the sorted list"""
        print(sorted(self))
