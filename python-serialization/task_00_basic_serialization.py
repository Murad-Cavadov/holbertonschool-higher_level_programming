#!/usr/bin/env python3
"""
Bu modul əsas seriyallaşdırma funksiyalarını ehtiva edir.
Lüğəti JSON faylına çevirir və fayldan yenidən lüğət kimi oxuyur.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Python lüğətini JSON formatında fayla yadda saxlayır.

    Args:
        data (dict): Seriyallaşdırılacaq məlumat lüğəti.
        filename (str): Çıxış faylının adı.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    JSON faylından məlumatı oxuyur və Python lüğətinə çevirir.

    Args:
        filename (str): Oxunacaq JSON faylının adı.

    Returns:
        dict: Deseriyallaşdırılmış məlumat.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
