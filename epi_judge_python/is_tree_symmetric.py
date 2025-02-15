from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Input:
# - A binary tree, tree: BinaryTreeNode

# Output
# is_bin_tree_symmetric: bool

# Notes / Assumptions
# - right-from-root traversal node_r
# - left-from-root traversal node_l
# ^ These are distinct

# - Recursively ensure that the left subtree of node_r is equal to the right subtree of node_l
# - Base case:
#   - (node_l.left == None and node_l.right == None) and (node_r.left == None and node_r.right == None)
#   - node_l != node_r

# Example


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def _is_mirror_equivalent(t1: BinaryTreeNode, t2: BinaryTreeNode):
        if not t1 and not t2:
            return True
        if (t1 and not t2) or (t2 and not t1) or (t1.data != t2.data):
            return False
        if (t1.left is None and t1.right is None) and (t2.left is None and t2.right is None):
            return True

        return _is_mirror_equivalent(t1.left, t2.right) and _is_mirror_equivalent(t1.right, t2.left)

    return not tree or _is_mirror_equivalent(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
