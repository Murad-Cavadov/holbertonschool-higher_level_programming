#!/usr/bin/python3
"""
Unit tests for the complete Square class including the update method.
"""
import unittest
from models.square import Square


class TestSquareUpdate(unittest.TestCase):
    """Test suite for checking the update method of the Square class."""

    def test_update_args(self):
        """Test update method with positional arguments (*args)."""
        s = Square(5, 0, 0, 1)
        
        s.update(10)
        self.assertEqual(s.id, 10)

        s.update(1, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)

        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)

        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update method with keyword arguments (**kwargs)."""
        s = Square(5, 0, 0, 1)
        
        s.update(x=12)
        self.assertEqual(s.x, 12)

        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

        s.update(size=7, id=89, y=1)
        self.assertEqual(s.id, 89)


if __name__ == "__main__":
    unittest.main()
