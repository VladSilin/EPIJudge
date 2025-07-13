from typing import List

from test_framework import generic_test

# Input:
# sequence: List[int], a sequence of integers

# Output:
# longest_sequence_length: int, the length of the longest nondecreasing subsequence

# Notes / Assumptions:
# - Equal elements are nondecreasing
# - Elements are NOT required to follow eachother in the original sequence

# Example:
# sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
# longest_sequence_length = 4 ([0, 4, 10, 14], [0, 2, 6, 9])

# Outline:
# Given 1st element and length 0, what are the possible actions?
#   - Take the element
#   - Leave the element

# Generalized:

# Given i'th element and length l, what are the possible actions?
#   - Take the element (i += 1, l += 1)
#   - Leave the element (i += 1)


def longest_nondecreasing_subsequence_length_no_dp(A: List[int]) -> int:
    def longest_given_element_and_last_length(i: int, last_elem: int):
        if i == len(A):
            return 0

        take = 0
        if A[i] >= last_elem:
            take = 1 + longest_given_element_and_last_length(i + 1, A[i])

        skip = longest_given_element_and_last_length(i + 1, last_elem)
        return max(take, skip)

    return longest_given_element_and_last_length(0, float("-inf"))


def longest_nondecreasing_subsequence_length0(A: List[int]) -> int:
    dp = {}

    def longest_given_element_and_last_length(i: int, last_elem: int):
        key = (i, last_elem)

        if key in dp:
            return dp[key]
        if i == len(A):
            return 0

        take = 0
        if A[i] >= last_elem:
            take = 1 + longest_given_element_and_last_length(i + 1, A[i])

        skip = longest_given_element_and_last_length(i + 1, last_elem)

        dp[key] = max(take, skip)
        return dp[key]

    return longest_given_element_and_last_length(0, float("-inf"))


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    max_length = [1] * len(A)

    for i in range(1, len(A)):
        max_length[i] = max(
            1 + max([max_length[j] for j in range(i) if A[i] >= A[j]], default=0),
            max_length[i],
        )

    return max(max_length)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            "longest_nondecreasing_subsequence.tsv",
            longest_nondecreasing_subsequence_length,
        )
    )
