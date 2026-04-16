#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    # sys.argv[1:] skriptin adından sonrakı bütün arqumentləri götürür
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
