#!/usr/bin/python3
"""this module contains a function that writes a string
to a text file (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
     the number of characters written"""
    with open(filename, "w", encoding="utf_8") as file:
        return file.write(text)
