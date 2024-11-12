from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    lowest_found_index = -1

    start = 0
    end = len(A)

    while start < end:
        mid = start + ((end - start) // 2)

        if k < A[mid]:
            end = mid
        elif k > A[mid]:
            start = mid + 1
        else:
            lowest_found_index = mid
            end = mid

    return lowest_found_index


if __name__ == '__main__':
    # test_list = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    # print(search_first_of_k(test_list, 285))
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
