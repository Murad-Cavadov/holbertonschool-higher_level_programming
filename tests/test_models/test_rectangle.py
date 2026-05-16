#!/usr/bin/python3
"""
Unit tests for the complete Rectangle class including kwargs update.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for the Rectangle class."""

    def test_update_args(self):
        """Test the update method with positional arguments (*args)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test the update method with keyword arguments (**kwargs)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(r.height, 1)

        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)


if __name__ == "__main__":
    unittest.main()
