#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_nums = set()


    for num in my_list:

        if num not in unique_nums:

            unique_nums.add(num)

    result = sum(unique_nums)

    return result
