import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:
# node0: BinaryTreeNode
# node1: BinaryTreeNode

# Output:
# lowest_common_ancestor: BinaryTreeNode

# Notes / Assumptions:
# - Time complexity should only depends on the nodes' distance from the LCA
#   - There are 2 distances, one smaller one larger

# Examples:


# Outline:
def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    seen_parents = set()
    p0, p1 = node0, node1
    while p0 or p1:

        if p0:
            if p0 in seen_parents:
                return p0

            seen_parents.add(p0)
            p0 = p0.parent

        if p1:
            if p1 in seen_parents:
                return p1

            seen_parents.add(p1)
            p1 = p1.parent

    raise ValueError("node0 and node1 are not in the same tree")


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0), must_find_node(tree, node1))
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
