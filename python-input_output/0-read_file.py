#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it.
It focuses on safe file handling using the 'with' statement.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to standard output.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
