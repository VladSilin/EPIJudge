import math
from typing import List

from test_framework import generic_test, test_utils

# Input:
# input_set: List[int], a list representing a set

# Output:
# power_set: List[List[int]], a list of lists representing a set of all subsets of input_set

# Notes / Assumptions:
#
# Base Case:
# - A set is "formed"
#
# R. Step:
# - Grow set OR
# - Shrink set
#
# Step mechanism:
# - Index OR
# - List copy

# Examples:
# input_set = [0, 1, 2, 3]
# power_set = [[], [0], [1], [2], [0, 1], [0, 2], [0, 3], [0, 1, 2]]]


# {0, 1, 2}
# gen(tbs = 0, ssf = [])
#   gen(tbs = 1, ssf = [])
#     gen(tbs = 2, ssf = [])
#       gen(tbs = 3, ssf = [])
#         append([]), return  ->  [[]]
#       gen(tbs = 3, [2])
#         append([2]), return  ->  [[], [2]]
#     gen(tbs = 2, ssf = [1])
#       gen(tbs = 3, ssf = [1])
#         append([1]), return  -> [[], [2], [1]]
#       gen(tbs = 3, ssf = [1, 2])
#         append([1, 2]), return  ->  [[], [2], [1], [1, 2]]
#   gen(tbs = 1, ssf = [0])
#     gen(tbs = 2, ssf = [0])
#       gen(tbs = 3, ssf = [0])
#         append([0]), return  ->  [[], [2], [1], [1, 2], [0]]
#       gen(tbs = 3, ssf = [0, 2])
#         append([0, 2]) return  ->  [[], [2], [1], [1, 2], [0], [0, 2]]
#     gen(tbs = 2, ssf = [0, 1])
#       gen(tbs = 3, ssf = [0, 1])
#         append([0, 1]), return  ->  [[], [2], [1], [1, 2], [0], [0, 2], [0, 1]]
#       gen(tbs = 3, ssf = [0, 1, 2])
#         append([0, 1, 2]) return  ->  [[], [2], [1], [1, 2], [0], [0, 2], [0, 1], [0, 1, 2]]
def generate_power_set0(input_set: List[int]) -> List[List[int]]:
    power_set = []

    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(
            to_be_selected + 1, selected_so_far + [input_set[to_be_selected]]
        )

    directed_power_set(0, [])
    return power_set


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    power_set = []

    for int_for_subset in range(1 << len(input_set)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1

        power_set.append(subset)

    return power_set


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
