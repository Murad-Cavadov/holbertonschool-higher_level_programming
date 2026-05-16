#!/usr/bin/python3
"""
Unit tests for the complete Base class including to_json_string method.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test suite for the Base class."""

    def test_auto_id(self):
        """Test automatic id incrementation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_explicit_id(self):
        """Test assigning specific integer id."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_to_json_string_none(self):
        """Test to_json_string with None argument."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with a valid list of dictionaries."""
        d = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_str = Base.to_json_string(d)
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')


if __name__ == "__main__":
    unittest.main()
