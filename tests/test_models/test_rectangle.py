#!/usr/bin/python3
"""
Unit tests for Rectangle class Task 2.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class initialization."""

    def test_rectangle_is_base(self):
        """Test if Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_rectangle_initialization(self):
        """Test valid width, height and default coordinates."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_explicit_id(self):
        """Test passing explicit id to Rectangle."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)


if __name__ == "__main__":
    unittest.main()
