#!/usr/bin/python3
"""
This module takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    # Sorğunu POST metodu ilə göndəririk
    response = requests.post(
        url, data=payload, headers={'cfclearance': 'true'}
    )
    print(response.text)
