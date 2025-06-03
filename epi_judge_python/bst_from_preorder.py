from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

# Input:
# preorder_sequence: List[int]

# Output:
# result: BstNode

# Notes / Assumptions:
# - All nodes contain distinct data

# Examples:

# [1, 3, 5, 7, 9, 10]

#                  5
#                /   \
#               3     7
#             /  \     \
#            1          9
#                        \
#                        10

#                  7
#                /   \
#               5     9
#             /        \
#            3         10
#           /
#          1

# Outline:


def rebuild_bst_from_preorder0(preorder_sequence: List[int]) -> Optional[BstNode]:
    if not preorder_sequence:
        return None

    # TODO: Add to notes (use `next()` with list comprehension (genexp) to get first element satisfying a condition)
    #
    # transition_point = next((i for i, a in enumerate(preorder_sequence)
    #   if a > preorder_sequence[0]),
    #   len(preorder_sequence))
    root = preorder_sequence[0]
    i = 1

    while i < len(preorder_sequence) and preorder_sequence[i] < root:
        i += 1

    transition_index_to_right_subtree_nodes = i

    return BstNode(
        root,
        rebuild_bst_from_preorder(
            preorder_sequence[1:transition_index_to_right_subtree_nodes]
        ),
        rebuild_bst_from_preorder(
            preorder_sequence[transition_index_to_right_subtree_nodes:]
        ),
    )


def rebuild_bst_from_preorder1(preorder_sequence: List[int]) -> Optional[BstNode]:
    if not preorder_sequence:
        return None

    transition_point = next(
        (i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]),
        len(preorder_sequence),
    )

    return BstNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder(preorder_sequence[transition_point:]),
    )


def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    root_idx = [0]

    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None

        root_idx[0] += 1
        # Note that rebuild_bst_from_preorder_on_value_range() updates root_idx[0]
        # so the order of following two calls is critical.
        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)

        return BstNode(root, left_subtree, right_subtree)

    return rebuild_bst_from_preorder_on_value_range(float("-inf"), float("inf"))


if __name__ == "__main__":
    # test = BstNode(5)
    # test.left = BstNode(3)
    # test.right = BstNode(7)
    # test.left.left = BstNode(1)
    # test.right.right = BstNode(9)
    # test.right.right.right = BstNode(10)
    #
    # def preorder(tree):
    #     if not tree:
    #         return []
    #
    #     return [tree.data] + preorder(tree.left) + preorder(tree.right)
    #
    # res = preorder(test)
    # print(res)
    #
    # print(preorder(rebuild_bst_from_preorder(res)))

    exit(
        generic_test.generic_test_main(
            "bst_from_preorder.py", "bst_from_preorder.tsv", rebuild_bst_from_preorder
        )
    )
