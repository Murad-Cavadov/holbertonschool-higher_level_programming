#!/usr/bin/python3
"""
Bu modul matrisin elementlərini bölən funksiyanı ehtiva edir.
Bütün elementlər bir ədədə bölünür və nəticə yuvarlaqlaşdırılır.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür.

    Arqumentlər:
        matrix: Siyahılardan ibarət siyahı (int/float).
        div: Bölən ədəd (int/float).

    Returns:
        Nəticələrdən ibarət yeni matris.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        
        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix
