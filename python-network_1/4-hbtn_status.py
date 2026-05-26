#!/usr/bin/python3
"""
This module fetches https://intranet.hbtn.io/status
using the requests package and displays the body of the response.
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    # Firewall maneəsini keçmək üçün header əlavə edirik
    response = requests.get(url, headers={'cfclearance': 'true'})
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
