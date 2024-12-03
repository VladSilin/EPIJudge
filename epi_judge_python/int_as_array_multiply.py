from typing import List

from test_framework import generic_test

from itertools import zip_longest

# Input:
# num1: List[int] (represents int, MSD first, 0th elem can be -'ve)
# num2: List[int] (represents int, MSD first, 0th elem can be -'ve)

# Return:
# result: List[int] (array representing the product of the multiplication)

# Notes / Assumptions
# - MSD is first
# - 0th elem can be -'ve

# Example:
#
#   125
# * 229
# -----
#   250
#  2500
# 25000
# 27750

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if not num1 or not num2:
        return []

    intermediates = []
    for i in range(len(num2) - 1, -1, -1):
        intermediate = [0] * (len(num2) - 1 - i)
        carry = 0
        for j in range(len(num1) - 1, -1, -1):
            inter_result = abs(num2[i]) * abs(num1[j]) + carry
            carry = inter_result // 10
            inter_result = inter_result % 10

            intermediate.append(inter_result)

            if j == 0 and carry > 0:
                intermediate.append(carry)

        intermediates.append(intermediate)

    # TODO: Look into Python iterators more (i.e. why the need to wrap in list())
    # TODO: Add to notes (zip_longest())
    assoc_digits = list(zip_longest(*intermediates, fillvalue=0))
    carry = 0
    number = []
    for i in range(len(assoc_digits)):
        total = sum(assoc_digits[i]) + carry
        carry = total // 10
        number.append(total % 10)

        if i == len(assoc_digits) - 1 and carry > 0:
            number.append(carry)

    number.reverse()

    # TODO: Add to notes (use of next() iterator)
    number = number[next((i for i, e in enumerate(number) if e != 0), len(number)):] or [0]

    is_negative = num1[0] * num2[0] < 0
    if is_negative:
        number[0] = -number[0]

    return number


if __name__ == '__main__':
    #input1 = [-9, 9, 9]
    #input2 = [-1, 1]

    #result = multiply(input1, input2)

    #print(result)

    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
