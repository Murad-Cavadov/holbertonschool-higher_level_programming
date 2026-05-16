#!/usr/bin/python3
"""
Unit tests for the Square class.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square class."""

    def test_valid_init(self):
        """Test initialization variants for Square."""
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 1)

    def test_invalid_types(self):
        """Test string inputs raise TypeError."""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_invalid_values(self):
        """Test bad integer inputs raise ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test string layout representation."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_to_dict(self):
        """Test dictionary export output."""
        s = Square(1, 2, 3, 4)
        self.assertIsInstance(s.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
