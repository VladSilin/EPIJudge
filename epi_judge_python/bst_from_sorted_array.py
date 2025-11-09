import functools
import math
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import binary_tree_height, generate_inorder
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:
# A: List[int], a sorted list

# Output:
# min_height_bst: BstNode

# Notes / Assumptions:

# Examples:
# [1, 2, 3]

# Outline:
# - Brute Force: For n = Node(entry i), can put it at node [0 .. i - 1].left, .right, or parent
#
# - Itereate from left, right toward the median


def build_min_height_bst_from_sorted_array0(A: List[int]) -> Optional[BstNode]:
    def get_median_node(A):
        if not A:
            return None

        median_idx = len(A) // 2
        median = A[median_idx]

        return BstNode(
            median,
            get_median_node(A[:median_idx]),
            get_median_node(A[median_idx + 1 :]),
        )

    return get_median_node(A)


def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    def get_median_node(start, end):
        if start >= end:
            return None

        median_idx = start + (end - start // 2)
        median = A[median_idx]

        return BstNode(
            median,
            get_median_node(0, median_idx),
            get_median_node(median_idx + 1, end),
        )

    return get_median_node(A)


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py",
            "bst_from_sorted_array.tsv",
            build_min_height_bst_from_sorted_array_wrapper,
        )
    )
