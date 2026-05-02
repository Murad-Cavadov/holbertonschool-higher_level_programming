#!/usr/bin/env python3
"""
Bu modulda Shape abstrakt sinfi, Circle, Rectangle sinifləri 
və duck typing nümayişi üçün shape_info funksiyası yerləşir.
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Bütün formalar üçün blueprint (eskiz) təşkil edən abstrakt sinif."""

    @abstractmethod
    def area(self):
        """Sahəni hesablamalıdır."""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimetri hesablamalıdır."""
        pass

class Circle(Shape):
    """Dairə sinfi."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Düzbucaqlı sinfi."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Duck typing istifadə edərək obyektin tipini yoxlamadan 
    onun metodlarını çağırır.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
