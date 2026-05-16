#!/usr/bin/python3
"""
Unit tests for the Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test suite for Base class."""

    def test_auto_id(self):
        """Test auto id assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_saving_id(self):
        """Test explicit id saving."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test to_json_string with valid dict."""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        """Test from_json_string with valid string."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])


if __name__ == "__main__":
    unittest.main()
