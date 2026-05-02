#!/usr/bin/env python3
"""
Bu modulda Animal abstrakt sinfi və onun Dog, Cat alt sinifləri təyin olunub.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """Animal abstrakt əsas sinfi."""
    
    @abstractmethod
    def sound(self):
        """Hər bir alt sinif tərəfindən tətbiq edilməli olan abstrakt metod."""
        pass

class Dog(Animal):
    """Animal sinfindən törəyən Dog sinfi."""
    
    def sound(self):
        """İt səsini qaytarır."""
        return "Bark"

class Cat(Animal):
    """Animal sinfindən törəyən Cat sinfi."""
    
    def sound(self):
        """Pişik səsini qaytarır."""
        return "Meow"
