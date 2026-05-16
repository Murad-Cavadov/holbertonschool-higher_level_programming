#!/usr/bin/python3
"""
Defines a Square class with size getter and setter.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieves the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square, updating both width and height.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the print() and str() string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
