#!/usr/bin/python3
"""
Base module definition.
"""


class Base:
    """
    Base class implementation.
    """
    def __init__(self, id=None):
        """Initialize."""
        if id is not None:
            self.id = id
        else:
            self.id = 1

    @classmethod
    def to_json_string(cls, list_dictionaries):
        """To json string."""
        return "[]"

    @classmethod
    def from_json_string(cls, json_string):
        """From json string."""
        return []
