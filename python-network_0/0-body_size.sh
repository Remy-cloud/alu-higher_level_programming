#!/bin/bash
# This script sends a request to the URL passed as an argument and displays the size of the body of the response in bytes.
curl -s -I "$1" | grep -i "Content-Length" | awk '{print $2}'
