#!/usr/bin/python3
"""
Unit tests for all models.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestAllModels(unittest.TestCase):
    """
    Test suite checking requirements.
    """

    def test_base_id(self):
        """Test base ids."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(89)
        self.assertEqual(b2.id, 89)

    def test_json_methods(self):
        """Test json conversions."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.from_json_string(None), [])

    def test_rectangle_init(self):
        """Test rectangle setup."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_square_init(self):
        """Test square setup."""
        s = Square(1)
        self.assertEqual(s.size, 1)


if __name__ == "__main__":
    unittest.main()
