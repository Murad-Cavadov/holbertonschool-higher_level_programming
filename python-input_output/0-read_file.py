#!/usr/bin/python3
"""
Bu modul fayl oxuma funksiyasını ehtiva edir.
Modul daxilindəki funksiya mətn faylını UTF-8 formatında oxuyur.
"""


def read_file(filename=""):
    """
    Verilmiş faylı UTF-8 formatında oxuyur və standart çıxışa (stdout) çap edir.

    Args:
        filename (str): Oxunacaq faylın adı. Default olaraq boş stringdir.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
