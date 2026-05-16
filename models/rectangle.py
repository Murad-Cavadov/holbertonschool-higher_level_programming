#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle. Inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute."""
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute."""
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute."""
        self.__y = value
