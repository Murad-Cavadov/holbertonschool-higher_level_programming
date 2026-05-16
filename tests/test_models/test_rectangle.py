#!/usr/bin/python3
"""
Unit tests for the complete Rectangle class including to_dictionary method.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleDictionary(unittest.TestCase):
    """Test suite for checking the to_dictionary method of Rectangle."""

    def test_to_dictionary_output(self):
        """Test the dictionary structure and values."""
        r = Rectangle(10, 2, 1, 9, 5)
        r_dict = r.to_dictionary()
        
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertEqual(r_dict, expected)
        self.assertIsInstance(r_dict, dict)

    def test_to_dictionary_update(self):
        """Test that update method works correctly with dictionary output."""
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)


if __name__ == "__main__":
    unittest.main()
