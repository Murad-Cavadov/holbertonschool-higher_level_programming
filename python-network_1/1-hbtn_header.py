#!/usr/bin/python3
"""
This module takes in a URL, sends a request to it
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={'cfclearance': 'true'})

    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
