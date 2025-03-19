from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

# Input:
# - tree: BinaryTreeNode, the root node of the tree

# Output:
# - result: List[int], inorder traversal of the nodes
# - O(1) space

# Notes / Assumptions:
# - Nodes have parent pointers

# Example:

# Brute Force Outline:

# Optimized Outline:

# TODO: Add to notes:
#  - When implementing recursion iteratively:
#      - Loop iterations can represent stack frames
#      - Outer variables can represent parameters
#      - Need some way of representing / "remembering" which operation to be in in a given "stack frame"
#  - Here, how we "arrived" at the node in a given iteration is used to keep track of operation state
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []

    # NOTE: It matters how you got to the node, not whether the node is left or right
    prev, cur = None, tree
    while cur:
        # Came down from parent
        if prev is cur.parent:
            if cur.left:
                prev = cur
                cur = cur.left
            else:
                result.append(cur.data)

                # Key point
                prev = cur
                cur = cur.right or cur.parent
        # Came up from left child
        elif prev is cur.left:
            result.append(cur.data)

            prev = cur
            cur = cur.right or cur.parent
        # Came up from right child (done)
        #else
        elif prev is cur.right:
            prev = cur
            cur = cur.parent

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
