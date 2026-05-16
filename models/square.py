#!/usr/bin/python3
"""
Square module definition.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class implementation.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter."""
        self.width = value
        self.height = value
