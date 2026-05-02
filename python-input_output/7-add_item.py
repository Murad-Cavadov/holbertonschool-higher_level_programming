#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a JSON file.
This script uses functions from previous tasks to handle JSON data.
"""
import sys
import os


# Əvvəlki tapşırıqlardakı funksiyaları import edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Fayl mövcuddursa, içindəki siyahını yükləyirik
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    # Fayl yoxdursa, boş siyahı yaradırıq
    items = []

# Terminaldan gələn arqumentləri (skriptin adından başqa) siyahıya əlavə edirik
# sys.argv[0] skriptin adıdır, ona görə [1:] istifadə edirik
items.extend(sys.argv[1:])

# Yenilənmiş siyahını fayla yazırıq
save_to_json_file(items, filename)
