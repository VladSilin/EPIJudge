from typing import List

from test_framework import generic_test

# Input:
# A: List[int], a list of cyclically shifted elements

# Output:
# smallest: int, the smallest element (i.e. what would be the 1st element)

# Notes / Assumptions:
# - Can do a binary search for pairs of elements?
# - All elements are distinct

# Examples:
# [L, L, L, x, L, L, L, L]
#  l                    h
#
# [6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5]


# Outline:
def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A) - 1

    while left < right:
        mid = left + (right - left) // 2

        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )
