#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit
if number < 0:
    last_digit = -(-number % 10)  # Handle negative numbers
else:
    last_digit = number % 10

# Print the output based on the last digit
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")