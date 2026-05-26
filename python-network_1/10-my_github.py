#!/usr/bin/python3
"""
This module takes GitHub credentials (username and token) and uses
the GitHub API to display the user's account ID.
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    # Basic Authentication istifadə edərək sorğu göndəririk
    response = requests.get(
        url,
        auth=(username, token),
        headers={'cfclearance': 'true'}
    )

    try:
        json_data = response.json()
        print(json_data.get("id"))
    except ValueError:
        print("None")
