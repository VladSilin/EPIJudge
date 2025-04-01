from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# Input:
# - preorder: List[int], list values from preorder traversal of tree
# - inorder: List[int], list values from inorder traversal of tree

# Output:
# - result: BinaryTreeNode, the tree that generated the 2 traversal lists

# Notes / Assumptions:
# - Each node has a unique key
# - Find nodes where the 2 traversals converge?
# - What if the 2 provided lists don't actually represent the same tree?
#     - Is being able to tell this the first step?

# Example:
# - Why can 2 trees share an inorder traversal?
#               1               2
#              /             /   \
#             2             3     1
#
#
#            /
#           3

# Brute Force Outline:

# Optimized Outline:
# - At each step, 1 or more of the lists contain info on which node to insert at left or right
# - Things to the left of root in io tell about left subtree, things to the right tell about right subtree
# - The next elem. in po is adjacent to the prev. Question is, is it left or right?
# step 0: tree = po[0]
# step 1: What is tree.left?

# TODO: Add to notes (the traversals (preorder, inorder, postorder)) are named for the order in which the visit occurs
#  in relation to visiting the left and right SUBTREES)
def binary_tree_from_preorder_inorder0(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    root_val = preorder.pop(0)
    root = BinaryTreeNode(root_val)
    i = inorder.index(root_val)

    def _reconstruct(cur: BinaryTreeNode, nxt: BinaryTreeNode, idx: int):
        nxt = preorder.pop(0)
        found_at = inorder.index(nxt)
        is_left = found_at < idx

        if is_left:
            cur.left = nxt
        else:
            cur.right = nxt

        cur = nxt
    # TODO - you fill in here.
    return BinaryTreeNode()

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # TODO: Add to notes (construct a reverse index map)
    node_to_io_idx = { data: i for i, data in enumerate(inorder) }

    def _reconstruct(po_start, po_end, io_start, io_end):
        if po_end <= po_start or io_end <= io_start:
            return None

        root = preorder[po_start]

        # TODO: Optimize this
        root_idx = node_to_io_idx[root]

        # TODO: Add to notes (when using index as recursive step, remember to refer to e.g. 'start' rather than just '0')
        left_num = root_idx - io_start

        return BinaryTreeNode(root,
            _reconstruct(po_start + 1, po_start + left_num + 1, io_start, root_idx),
            _reconstruct(po_start + left_num + 1, po_end, root_idx + 1, io_end)
        )

    return _reconstruct(0, len(preorder), 0, len(inorder))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
