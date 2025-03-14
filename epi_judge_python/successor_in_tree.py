import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

# Inputs
# - node: BinaryTreeNode; A node of a binary tree

# Output
# - node: BinaryTreeNode; The successor of the given node in an inorder traversal

# Notes / Assumptions
# - Nodes have parent pointers

# Example

# Brute Force Outline
# - Traverse parent pointers back to root
# - Do inorder traversal, store the nodes (O(N) time, O(N) space, N nodes)
# - Iterate through list of nodes, return the successor

# Optimized Outline
# - Assume the given node is the root of a tree
#     - Would the successor be left or right of it?
#         - Neither, could be above
def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left

        return cur

    cur = node
    while cur.parent and cur.parent.right is cur:
        cur = cur.parent

    return cur.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
