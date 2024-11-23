#!/usr/bin/python3
#This script makes a request and displays a response using the requests package.
import requests

if __name__ == "__main__":
    # URL to fetch the response from
    url = 'https://alu-intranet.hbtn.io/status'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Display the body of the response with the required tabulation
    print("Body response:")
    print("\t- {}".format(response.text))
