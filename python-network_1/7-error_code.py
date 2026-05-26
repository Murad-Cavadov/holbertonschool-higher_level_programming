#!/usr/bin/python3
"""
This module takes in a URL, sends a request to it, and displays the
body of the response. It handles HTTP status codes greater than or
equal to 400.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url, headers={'cfclearance': 'true'})

    # Status kodunun 400 və ya daha böyük olmasını yoxlayırıq
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
