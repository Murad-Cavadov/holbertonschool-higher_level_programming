#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file.
It returns the total number of characters written to the file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns characters count.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
