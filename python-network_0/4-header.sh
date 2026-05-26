#!/bin/bash
# Sends a GET request to a URL with a header variable and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
