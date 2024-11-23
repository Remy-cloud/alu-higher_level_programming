#!/usr/bin/python3
"""
This script fetches the status from a given URL using the urllib library.
"""

import urllib.request

if __name__ == "__main__":
    # The URL from which we are fetching data
    url = "https://alu-intranet.hbtn.io/status"
    
    # Using 'with' statement to ensure proper closing of the response
    with urllib.request.urlopen(url) as request:
        print("Body response:")
        
        # Reading the response data
        data = request.read()
        
        # Displaying the type of the response data
        print("\t- type: {}".format(type(data)))
        
        # Displaying the raw content (bytes) of the response
        print("\t- content: {}".format(data))
        
        # Decoding the bytes to utf-8 to show the human-readable content
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
