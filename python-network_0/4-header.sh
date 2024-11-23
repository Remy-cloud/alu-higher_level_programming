#!/bin/bash
# Script that sends GET request with custom header X-HolbertonSchool-User-Id: 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "http://127.0.0.1:5000$1"
