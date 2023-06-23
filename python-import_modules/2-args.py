#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    print("{:d} argument{}".format(num, "" if num == 1 else "s"), end="")
    print("{}".format("." if num == 0 else ":"))
    if num > 0:
        for i in range(1, num + 1):
            print("{:d}: {}".format(i, argv[i]))
