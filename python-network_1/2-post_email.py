#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Prepare the data to send in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Send the POST request and get the response
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print(body)
