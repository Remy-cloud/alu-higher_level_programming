#!/bin/bash
# Script that sends GET request with custom header X-HolbertonSchool-User-Id: 98
curl -sH "X-HolbertonSchool-User-Id: 98" "http://0.0.0.0:5000$1"
