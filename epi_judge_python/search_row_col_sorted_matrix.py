from typing import List

from test_framework import generic_test

# Input:
# A: List[List[int]]

# Output:
# is_in_array: bool

# Notes / Assumptions:
# - Is the array N x N?

# Example:

# Brute Force:
# - Iterate through each row, each element
#   - Check if the element is equal to x

# Outline:


def matrix_search(A: List[List[int]], x: int) -> bool:
    if not A:
        return False

    last_row, last_col = 0, len(A[0]) - 1

    while last_row < len(A) and last_col >= 0:
        corner = A[last_row][last_col]
        if x > corner:
            last_row += 1
        elif x < corner:
            last_col -= 1
        else:
            # x == corner, element found
            return True

    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_row_col_sorted_matrix.py",
            "search_row_col_sorted_matrix.tsv",
            matrix_search,
        )
    )
