#!/usr/bin/python3
"""
Unit tests for the complete Rectangle class including update method.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for the Rectangle class."""

    def test_update_args(self):
        """Test the update method with positional arguments (*args)."""
        r = Rectangle(10, 10, 10, 10, 1)
        
        r.update(89)
        self.assertEqual(r.id, 89)

        r.update(89, 2)
        self.assertEqual(r.width, 2)

        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)


if __name__ == "__main__":
    unittest.main()
