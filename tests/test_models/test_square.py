#!/usr/bin/python3
"""
Unit tests for the Square class functionality.
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test suite for the Square class."""

    def test_square_is_rectangle(self):
        """Test if Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_square_initialization(self):
        """Test valid initialization and values."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)

    def test_square_area(self):
        """Test inherited area method for Square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_str(self):
        """Test __str__ output format for Square."""
        s = Square(5, 1, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 1/3 - 5")

    def test_invalid_size_type(self):
        """Test that invalid size type raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")


if __name__ == "__main__":
    unittest.main()
