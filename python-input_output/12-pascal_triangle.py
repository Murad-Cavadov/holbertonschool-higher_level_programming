#!/usr/bin/python3
"""
Bu modul n ölçülü Paskal üçbucağını qaytaran funksiyanı ehtiva edir.
"""


def pascal_triangle(n):
    """
    n ölçülü Paskal üçbucağını siyahıların siyahısı şəklində qaytarır.

    Args:
        n (int): Üçbucağın sətir sayı.

    Returns:
        list: Tam ədədlərdən ibarət siyahıların siyahısı.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Hər yeni sətrin əvvəlinə 1 qoyuruq
        row = [1]
        # Əvvəlki sətri götürürük
        prev_row = triangle[i - 1]

        # Aradakı elementləri hesablayırıq
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # Hər sətrin sonuna 1 əlavə edirik
        row.append(1)
        triangle.append(row)

    return triangle
