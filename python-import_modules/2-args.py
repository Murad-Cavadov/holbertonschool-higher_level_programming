#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # sys.argv[0] skriptin adıdır, ona görə len(sys.argv) - 1 arqumentlərin sayıdır
    n = len(sys.argv) - 1

    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))
