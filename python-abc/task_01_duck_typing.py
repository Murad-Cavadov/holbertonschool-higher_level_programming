#!/usr/bin/env python3
"""
Abstrakt siniflər və Duck Typing nümunəsi.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape abstrakt sinfi."""

    @abstractmethod
    def area(self):
        """Sahə metodu."""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimetr metodu."""
        pass


class Circle(Shape):
    """Circle sinfi."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle sinfi."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Obyektin area və perimeter metodlarını çağırıb nəticəni çap edir."""
    # Şəkildəki output formatına tam uyğun olaraq:
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
