#!/usr/bin/python3
"""
Unit tests for the complete Base class including save_to_file method.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBaseFile(unittest.TestCase):
    """Test suite for checking file operations in Base class."""

    def tearDown(self):
        """Clean up generated files after each test."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")

    def test_save_to_file_none(self):
        """Test save_to_file with None as argument."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file with an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_valid(self):
        """Test save_to_file with valid Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertTrue(len(content) > 0)
            self.assertIn('"id": 1', content)


if __name__ == "__main__":
    unittest.main()
