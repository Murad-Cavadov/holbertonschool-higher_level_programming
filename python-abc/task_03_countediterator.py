#!/usr/bin/env python3
"""
Bu modulda CountedIterator sinfi yerləşir.
Bu sinif neçə elementin iterasiya edildiyini izləyir.
"""


class CountedIterator:
    """İterasiya edilən elementlərin sayını saxlayan iterator sinfi."""

    def __init__(self, iterable):
        """
        Başlanğıc dəyərləri təyin edir.
        self.iterator: verilən obyekti iteratora çevirir.
        self.counter: sayğacı sıfırlayır.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Hal-hazırda neçə elementin keçildiyini qaytarır."""
        return self.counter

    def __next__(self):
        """
        Növbəti elementi qaytarır və sayğacı bir vahid artırır.
        Əgər element bitibsə, StopIteration qaytarır.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            # Orijinal iterator bitəndə biz də StopIteration qaytarmalıyıq
            raise StopIteration

    def __iter__(self):
        """İterator obyektinin özünü qaytarır."""
        return self
