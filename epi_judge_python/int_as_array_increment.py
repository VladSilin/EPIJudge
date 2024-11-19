from typing import List

from test_framework import generic_test

# Inputs:
# A: List[int] (represents a non-negative decimal integer D)

# Return:
# List[int] representing the integer D + 1

# Example:
# A = [1, 2, 9]
# result = [1, 3, 0]

# [1, 2, 9]
# [1, 0, 0, 0]
# Case 1: LSD is < 9
# - Simply increment the digit and return
# Case 2: LSD == 9
# - Set LSD to 0, i -= 1
#     - If A[i] < 9
#         - Increment the digit and return
#     - else:
#         - Set to 0, i -= 1

# Notes / Assumptions:
# - Algorithm should work even if implemented with finite precision arithmetic

def plus_one(A: List[int]) -> List[int]:
    for i in range(len(A) - 1, -1, -1):
        if A[i] < 9:
            A[i] += 1
            return A
        else:
            A[i] = 0
            if i == 0:
                A.insert(0, 1)

    return A


if __name__ == '__main__':
    #input = [0, 0, 0, 0, 0]
    #result = plus_one(input)
    #print(result)

    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
