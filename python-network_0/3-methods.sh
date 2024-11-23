#!/bin/bash
# Script that displays HTTP methods the server accepts
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
