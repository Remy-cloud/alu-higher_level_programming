#!/bin/bash
# Script that sends GET request with custom header X-HolbertonSchool-User-Id: 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "http://localhost:5000$1"
