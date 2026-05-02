#!/usr/bin/python3
"""
This module contains a function that converts a JSON string
to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted into a Python object.

    Returns:
        any: Python data structure (list, dict, etc.)
    """
    return json.loads(my_str)
