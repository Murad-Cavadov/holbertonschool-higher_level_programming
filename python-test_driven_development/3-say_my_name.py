#!/usr/bin/python3
"""
Bu modul say_my_name funksiyasini ehtiva edir.
"""


def say_my_name(first_name, last_name=""):
    """
    'My name is <first name> <last name>' seklinde cap edir.

    Args:
        first_name: Birinci ad (string olmalidir).
        last_name: Soyad (string olmalidir, susmaya gore bosdur).

    Raises:
        TypeError: Eger ad ve ya soyad string deyilse.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
