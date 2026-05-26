#!/usr/bin/python3
"""
This module takes in a URL, sends a request to it
and displays the value of the X-Request-Id variable
found in the response header.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    # Firewall maneəsini keçmək üçün başlığı əlavə edirik
    response = requests.get(url, headers={'cfclearance': 'true'})
    print(response.headers.get("X-Request-Id"))
