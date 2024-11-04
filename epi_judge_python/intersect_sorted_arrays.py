from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    result_list = []

    i, j = 0, 0
    last_added = None
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
            continue
        elif A[i] > B[j]:
            j += 1
            continue
        else:
            if A[i] != last_added:
                result_list.append(A[i])
                last_added = A[i]

            i, j = i + 1, j + 1

    return result_list


if __name__ == '__main__':
    # list_a = [1, 2, 3, 4, 5, 6, 7, 8]
    #                                i
    # list_b =          [4, 5, 7, 7]
    #                             j
    # result = intersect_two_sorted_arrays(list_a, list_b)
    # print(result)
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
