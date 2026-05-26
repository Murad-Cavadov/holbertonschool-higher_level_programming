#!/usr/bin/python3
"""
This module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    
    # Arqument verilib-verilmədiyini yoxlayırıq
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}

    try:
        # Sorğunu göndəririk (firewall üçün header ilə birgə)
        response = requests.post(
            url, data=payload, headers={'cfclearance': 'true'}
        )
        
        # Gələn cavabı JSON olaraq oxumağa çalışırıq
        json_data = response.json()

        # JSON etibarlıdırsa, amma boşdursa
        if json_data == {}:
            print("No result")
        else:
            # Holberton tələbi: lüğətdən məlumatları .get() ilə çəkirik
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))

    except ValueError:
        # Əgər gələn cavab düzgün JSON formatında deyilsə
        print("Not a valid JSON")
