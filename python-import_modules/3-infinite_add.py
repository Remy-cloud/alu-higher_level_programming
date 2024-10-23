#!/usr/bin/python3
import sys

# Only execute the following when the script is run directly
if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    total = 0

    # Iterate through each argument, convert to integer, and add to total
    for arg in argv:
        total += int(arg)

    # Print the total sum of the arguments
    print("{}".format(total))
