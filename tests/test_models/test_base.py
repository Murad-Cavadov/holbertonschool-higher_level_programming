#!/usr/bin/python3
"""
Unit tests for the complete Base class including the create method.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseCreate(unittest.TestCase):
    """Test suite for checking the create method of the Base class."""

    def test_create_rectangle(self):
        """Test create method for Rectangle instance."""
        r1 = Rectangle(3, 5, 1, 0, 99)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create method for Square instance."""
        s1 = Square(5, 2, 2, 88)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
