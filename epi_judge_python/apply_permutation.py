from typing import List

from test_framework import generic_test

# Inputs:
# A: List[int], array of integers; perm: List[int], array of indices (mapping index to new index)

# Outputs:
# [in-place]: List[int]
# - Array with permutation applied

# Notes / Assumptions:
# - Num. elements in perm == num. elements in A
# - If i == perm[i], the position of A[i] remains unchanged
# - For all in perm, perm[i] < len(A)
#
# - max_index = 0
# - while not visited[max_index]:
#     - temp = A[perm[max_index]]
#     - Put the A[max_index] to A[perm[max_index]]
#     - max_index = perm[max_index]
#     - visited[max_index] = True
# - max_index += 1

# Example:
# A    = [a, b, c, d]
# perm = [2, 0, 1, 3]
#
# A    = [a, b, c, d]
# t = c
#
# [b, c, a, d]
#
# result = [b, c, a, d]
def apply_permutation(perm: List[int], A: List[int]) -> None:
    visited = [False] * len(A)

    i = 0
    while i < len(A):
        j = i
        cur = A[j]
        while not visited[j]:
            temp = A[perm[j]]
            A[perm[j]] = cur
            cur = temp

            visited[j] = True
            j = perm[j]

        i += 1


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    #input = ['a', 'b', 'c', 'd']

    #apply_permutation([0, 1, 2, 3], input)
    #print(input)

    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
