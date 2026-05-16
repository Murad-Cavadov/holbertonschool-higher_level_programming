#!/usr/bin/python3
"""
Unit tests for the complete Base class including load_from_file method.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseLoadFile(unittest.TestCase):
    """Test suite for checking file loading operations in Base class."""

    def tearDown(self):
        """Clean up generated files after each test."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file when the file does not exist."""
        output = Rectangle.load_from_file()
        self.assertEqual(output, [])

    def test_load_from_file_rectangle(self):
        """Test loading Rectangle instances from file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 1)
        self.assertEqual(str(output[0]), str(r1))
        self.assertIsInstance(output[0], Rectangle)

    def test_load_from_file_square(self):
        """Test loading Square instances from file."""
        s1 = Square(5, 1, 2, 9)
        Square.save_to_file([s1])
        output = Square.load_from_file()
        self.assertEqual(len(output), 1)
        self.assertEqual(str(output[0]), str(s1))
        self.assertIsInstance(output[0], Square)


if __name__ == "__main__":
    unittest.main()
