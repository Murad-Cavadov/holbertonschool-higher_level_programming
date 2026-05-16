#!/usr/bin/python3
"""
Unit tests for the Square class size getter, setter, and validation.
"""
import unittest
from models.square import Square


class TestSquareSize(unittest.TestCase):
    """Test suite for the Square class size feature."""

    def test_size_getter_and_setter(self):
        """Test accessing and modifying the size attribute."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_invalid_type(self):
        """Test that invalid size type raises TypeError with width message."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_invalid_value(self):
        """Test that invalid size value raises ValueError with width message."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -5
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


if __name__ == "__main__":
    unittest.main()
