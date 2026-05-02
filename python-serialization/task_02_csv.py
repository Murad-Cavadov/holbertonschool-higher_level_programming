#!/usr/bin/env python3
"""
Bu modul CSV məlumatlarını JSON formatına çevirmək üçün
funksiyanı ehtiva edir.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur və onu 'data.json' adlı fayla
    JSON formatında yazır.

    Args:
        csv_filename (str): Oxunacaq CSV faylının adı.

    Returns:
        bool: Çevrilmə uğurlu olduqda True, əks halda False.
    """
    data_list = []
    try:
        # CSV faylını oxuyuruq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            csv_reader = csv.DictReader(csv_f)
            for row in csv_reader:
                data_list.append(row)

        # JSON faylına yazırıq
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data_list, json_f, indent=4)

        return True
    except (FileNotFoundError, IOError, PermissionError):
        # Fayl tapılmadıqda və ya digər giriş-çıxış xətalarında
        return False
