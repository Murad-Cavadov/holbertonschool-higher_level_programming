#!/usr/bin/env python3
"""
Bu modul Multiple Inheritance (Çoxlu Mirasalma) nümunəsini ehtiva edir.
"""


class Fish:
    """Balıq sinfi."""

    def swim(self):
        """Üzmə metodu."""
        print("The fish is swimming")

    def habitat(self):
        """Yaşayış yeri metodu."""
        print("The fish lives in water")


class Bird:
    """Quş sinfi."""

    def fly(self):
        """Uçma metodu."""
        print("The bird is flying")

    def habitat(self):
        """Yaşayış yeri metodu."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Həm Fish, həm də Bird sinfindən miras alan FlyingFish sinfi."""

    def fly(self):
        """Bird sinfindən olan fly metodunu override edir."""
        print("The flying fish is soaring!")

    def swim(self):
        """Fish sinfindən olan swim metodunu override edir."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Hər iki valideynin habitat metodunu override edir."""
        print("The flying fish lives both in water and the sky!")
