#!/usr/bin/python3
"""
Unit tests for the complete Square class including to_dictionary method.
"""
import unittest
from models.square import Square


class TestSquareDictionary(unittest.TestCase):
    """Test suite for checking the to_dictionary method of Square."""

    def test_to_dictionary_output(self):
        """Test the dictionary structure and values for Square."""
        s = Square(10, 2, 1, 5)
        s_dict = s.to_dictionary()
        
        expected = {'id': 5, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s_dict, expected)
        self.assertIsInstance(s_dict, dict)

    def test_to_dictionary_update(self):
        """Test that update method works correctly with square dictionary."""
        s1 = Square(10, 2, 1, 5)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)


if __name__ == "__main__":
    unittest.main()
