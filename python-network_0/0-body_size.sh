#!/bin/bash
# Script that displays the size of the body of a URL response
curl -s "http://localhost:5000$1" | wc -c
