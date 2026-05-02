#!/usr/bin/python3
"""
This module contains a function that converts an object to its JSON
representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized into JSON string.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
