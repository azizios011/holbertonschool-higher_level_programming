#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    if ascii_value >= 97 and ascii_value <= 122:
        return True
    else:
        return False
