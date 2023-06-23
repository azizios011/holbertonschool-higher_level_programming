#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if len(my_list) > 0:
        for i in range(0, len(my_list)):
            test = 0
            for j in range(0, i):
                if my_list[i] == my_list[j]:
                    test = 1
            if test == 0:
                sum += my_list[i]
    return sum
