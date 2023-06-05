#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    output = "{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(
        a, b, result_add, a, b, result_sub, a, b, result_mul, a, b, result_div
    )

    print(output)

if __name__ == "__main__":
    main()
