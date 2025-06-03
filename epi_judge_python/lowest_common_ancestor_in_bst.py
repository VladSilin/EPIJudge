import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:
# tree: BstNode, the tree to process
# s: BstNode, node 1
# b: BstNode, node 2

# Output:
# lca: BstNode, the lowest common ancestor of s and 

# Notes / Assumptions:

# Example:

# Outline:


# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_lca0(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    path_to_s = set()

    def _find_node(tree, node: BstNode):
        if not tree or node.data == tree.data:
            return tree

        if node.data > tree.data:
            return _find_node(tree.right, node)
        else:
            return _find_node(tree.left, node)

    _find_node(tree, s)
    print(path_to_s)

    # TODO: Now look for the other node the same way while checking the path
    # (continuously updating the node which is seen on the path)


def find_lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    while tree.data < s.data or tree.data > b.data:
        # Keep searching since tree is outside of [s, b]
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left

    # Now, s.data <= tree.data && tree.data <= b.data
    return tree


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(
            find_lca, tree, must_find_node(tree, s), must_find_node(tree, b)
        )
    )
    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_in_bst.py",
            "lowest_common_ancestor_in_bst.tsv",
            lca_wrapper,
        )
    )
