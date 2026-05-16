#!/usr/bin/python3
"""
Defines a Square class with a to_dictionary method.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square that inherits from Rectangle with serialization.
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

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the Square instance using *args or **kwargs.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
