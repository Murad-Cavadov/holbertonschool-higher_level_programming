#!/usr/bin/python3
"""
Unit tests for the complete Base class including from_json_string method.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test suite for the Base class."""

    def test_auto_id(self):
        """Test automatic id incrementation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_from_json_string_none(self):
        """Test from_json_string with None argument."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        output = Base.from_json_string(json_str)
        self.assertIsInstance(output, list)
        self.assertEqual(output, [{'id': 89, 'width': 10, 'height': 4}])


if __name__ == "__main__":
    unittest.main()
