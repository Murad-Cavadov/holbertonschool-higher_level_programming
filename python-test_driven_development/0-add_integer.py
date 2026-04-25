#!/usr/bin/python3
"""
Bu modul iki tam ədədi toplayan funksiyanı ehtiva edir.
Funksiya float dəyərləri integer-ə çevirir.
"""


def add_integer(a, b=98):
    """
    İki ədədi (a və b) toplayır və nəticəni tam ədəd kimi qaytarır.
    
    Arqumentlər:
        a: integer və ya float
        b: integer və ya float (susmaya görə 98)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
