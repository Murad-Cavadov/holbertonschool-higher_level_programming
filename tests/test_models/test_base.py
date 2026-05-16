#!/usr/bin/python3
"""
Unit tests for Base class Task 1.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Task 1 Base implementation."""

    def test_auto_id(self):
        """Test automatic id incrementation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_explicit_id(self):
        """Test assigning specific integer id."""
        b = Base(12)
        self.assertEqual(b.id, 12)


if __name__ == "__main__":
    unittest.main()
