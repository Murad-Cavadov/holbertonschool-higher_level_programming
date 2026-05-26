#!/usr/bin/python3
"""
This module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}

    try:
        response = requests.post(
            url, data=payload, headers={'cfclearance': 'true'}
        )

        json_data = response.json()

        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))

    except ValueError:
        print("Not a valid JSON")
