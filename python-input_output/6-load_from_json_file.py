#!/usr/bin/python3
"""
This module contains a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the file to load the JSON from.

    Returns:
        any: The Python object represented by the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
