#!/usr/bin/python3
import urllib.request

# Define the URL
url = 'https://alu-intranet.hbtn.io/status'

# Use a with statement to handle the opening and closing of the URL
with urllib.request.urlopen(url) as response:
    # Read the body of the response
    body = response.read()

    # Display the body of the response with the required tabulation
    print("Body response:")
    print("\t- " + body.decode('utf-8'))

