#!/usr/bin/python3
"""
Rectangle module definition.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class implementation.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Area function."""
        return self.width * self.height

    def to_dictionary(self):
        """To dictionary function."""
        return {}
