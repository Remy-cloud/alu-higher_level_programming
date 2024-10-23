#!/usr/bin/python3
import sys

# Only execute the following when the script is run directly
if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    num_args = len(argv)  # Get the number of arguments

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # Print each argument with its position
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
