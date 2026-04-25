#!/usr/bin/python3
"""
Bu modul matrisi bolmek ucun funksiyani ehtiva edir.
"""


def matrix_divided(matrix, div):
    """
    Matrisin butun elementlerini div-e bolur.
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
