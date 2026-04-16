#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər bir kortej üçün ilk iki elementi götürürük, yoxdursa 0 təyin edirik
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    
    # Toplayıb yeni kortej qaytarırıq
    return (a1 + b1, a2 + b2)
