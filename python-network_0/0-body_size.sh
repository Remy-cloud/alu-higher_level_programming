#!/bin/bash
# Uses curl on the first argument and prints the size of it.
curl -s -X GET "$1" | wc -c
