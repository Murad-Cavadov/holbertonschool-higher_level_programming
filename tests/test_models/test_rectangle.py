#!/usr/bin/python3
"""
Unit tests for Rectangle class area method.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleArea(unittest.TestCase):
    """Test cases for checking the area method of Rectangle."""

    def test_area_calculation(self):
        """Test computing area with regular values."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


if __name__ == "__main__":
    unittest.main()
    def test_display(self):
        """Test display method output without x and y."""
        import io
        from unittest.mock import patch

        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
            def test_str_method(self):
        """Test the __str__ method output format."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")
