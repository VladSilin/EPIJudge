import collections
from typing import List

from test_framework import generic_test

# Input:
# A: List[int], a list of integers

# Output:
# most_consecutive_ints: int, largest subset of integers such that all consecutive integers are between them

# Notes / Assumptions:
# - Array is unsorted

# Outline:
# - Put all numbers into hasmap with count = 0
# - Iterate through, for each n check:
#   - If n - 1 in map
#   - increment count of n
# - Return max of counts

# Examples:


def longest_contained_range(A: List[int]) -> int:
    unprocessed_entries = set(A)

    most_consecutive_ints = 0
    while unprocessed_entries:
        num = unprocessed_entries.pop()

        lower_bound = num - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        upper_bound = num + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        most_consecutive_ints = max(
            most_consecutive_ints, upper_bound - lower_bound - 1
        )

    return most_consecutive_ints


if __name__ == "__main__":
    # input1 = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
    #
    # res1 = longest_contained_range(input1)

    exit(
        generic_test.generic_test_main(
            "longest_contained_interval.py",
            "longest_contained_interval.tsv",
            longest_contained_range,
        )
    )
