#!/usr/bin/env python3
"""
Bu modul xüsusi Python obyektlərinin pickle modulu ilə
seriyallaşdırılmasını təmin edir.
"""
import pickle


class CustomObject:
    """
    Ad, yaş və tələbə statusu olan xüsusi obyekt sinfi.
    """

    def __init__(self, name, age, is_student):
        """Obyekti verilən dəyərlərlə başladır."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin atributlarını tələb olunan formatda çap edir."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Obyektin mövcud instansiyasını fayla seriyallaşdırır.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, IOError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Fayldan CustomObject instansiyasını yükləyir və qaytarır.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (OSError, IOError, pickle.PickleError, EOFError):
            return None
