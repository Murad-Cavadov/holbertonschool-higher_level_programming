#!/usr/bin/python3
"""
Bu modul text_indentation funksiyasini ehtiva edir.
"""


def text_indentation(text):
    """
    Metni '.', '?' ve ':' simvollarindan sonra iki yeni setirle cap edir.
    Setrlerin evvelinde ve sonunda bosluq qalmamasini temin edir.

    Args:
        text: Cap edilmeli olan metn (string).

    Raises:
        TypeError: Eger text string deyilse.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Simvolu yoxlamaq ucun flag (bosluqlari idare etmek ucun)
    c = 0
    # Metnin evvelindeki ve sonundaki bosluqlari temizleyirik
    text = text.strip()

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            c += 1
            # Xususi simvoldan sonra gelen bosluqlari kecirik
            while c < len(text) and text[c] == " ":
                c += 1
            continue
        c += 1
