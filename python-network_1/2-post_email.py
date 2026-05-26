#!/usr/bin/python3
"""
This module takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    # Datay-ı URL formatına salıb baytlara çeviririk
    data = urllib.parse.urlencode(values).encode('utf-8')

    # Sorğunu hazırlayırıq (Sətir çox uzun olmasın deyə böldük)
    req = urllib.request.Request(
        url, data=data, headers={'cfclearance': 'true'}
    )

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
