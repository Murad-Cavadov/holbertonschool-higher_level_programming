#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Əgər simvol kiçik hərfdirsə (a-z)
        if ord(char) >= 97 and ord(char) <= 122:
            # ASCII-də kiçik və böyük hərf arasındakı fərq 32-dir
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")  # Sonda yeni sətir üçün
