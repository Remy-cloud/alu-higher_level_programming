#!/bin/bash
# This script sends a POST request to the URL passed as an argument with email and subject variables and displays the body of the response.
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
