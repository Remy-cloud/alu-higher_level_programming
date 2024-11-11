#!/usr/bin/python3
def read_file(filename=""):
    """this module contains a function that Reads a text file
     (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as file:
        """Opens the file using UTF-8 encoding and ensures 
        the file is properly closed after the block is executed."""
        print(file.read(), end="")
