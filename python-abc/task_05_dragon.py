#!/usr/bin/env python3
"""
Bu modulda Mixin-lərdən istifadə edərək Dragon sinfi yaradılıb.
"""


class SwimMixin:
    """Üzmə bacarığı əlavə edən Mixin."""

    def swim(self):
        """Üzmə mesajını çap edir."""
        print("The creature swims!")


class FlyMixin:
    """Uçma bacarığı əlavə edən Mixin."""

    def fly(self):
        """Uçma mesajını çap edir."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Həm SwimMixin, həm də FlyMixin-dən miras alan Dragon sinfi.
    Bu sinif həm uça, həm də üzə bilir.
    """

    def roar(self):
        """Əjdaha nəriltisini çap edir."""
        print("The dragon roars!")
