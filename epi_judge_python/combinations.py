from typing import List

from test_framework import generic_test, test_utils

# Inputs
# n: int, overall number of elements
# k: int, size of subsets

# Outputs
# subsets: List[List[int]], all subsets of the given size

# Notes / Assumptions

# Examples
# k = 2, n = 5
# [1, 2, 3, 4, 5]


# Outline

# k = 2, n = 5
# [1, 2, 3, 4, 5]


# c(1, [])
#   c(2, [1])
#     c(3, [1, 2])
#       append([1, 2]) -> [[1, 2]]
def combinations(n: int, k: int) -> List[List[int]]:
    result = []

    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(list(partial_combination))

        num_remaining = k - len(partial_combination)

        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combination + [i])
            i += 1

    directed_combinations(1, [])
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            "combinations.tsv",
            combinations,
            comparator=test_utils.unordered_compare,
        )
    )
