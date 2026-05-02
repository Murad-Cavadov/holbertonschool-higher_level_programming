#!/usr/bin/python3
"""
Bu modul JSONPlaceholder API-dan məlumat çəkmək və 
onları emal etmək üçün funksiyaları ehtiva edir.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    API-dan bütün postları çəkir və başlıqlarını (title) çap edir.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Postları çəkir və onları 'posts.csv' faylına yadda saxlayır.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # Yalnız lazım olan sütunları (id, title, body) seçirik
        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        # CSV faylına yazırıq
        filename = "posts.csv"
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
