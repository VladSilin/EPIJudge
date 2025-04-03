import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:
# tree: BinaryTreeNode, root node of a bin. tree (no parent ref.)

# Output:
# exterior: List[BinaryTreeNode], list of [*[root to left leaf], *[leaves], *[right leaf to root]]

# Notes / Assumptions:
# - Leftmost leaf: 1st in inorder traversal
# - Rightmost leaf: last in inorder traversal

# Brute Force Outline:
# - Traverse node.left until node == None

# Optimized Outline:

# Example:

def exterior_binary_tree0(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    exterior = []
    def preorder(t: BinaryTreeNode):
        if t is None:
            return

        exterior.append(t)
        preorder(t.left) if t.left else preorder(t.right)

    def mod_inorder(t: BinaryTreeNode):
        if t is None:
            return

        mod_inorder(t.left)
        if t.left is None and t.right is None and t is not exterior[len(exterior) - 1]:
            exterior.append(t)
        mod_inorder(t.right)


    def postorder(t: BinaryTreeNode, last_idx):
        if t is None:
            return

        print(exterior[last_idx])
        if not exterior or t is not exterior[last_idx] and t is not exterior[0]:
            postorder(t.right, last_idx) if t.right else postorder(t.left, last_idx)
            exterior.append(t)

    preorder(tree)
    mod_inorder(tree)
    last_node_idx = len(exterior) - 1
    print(last_node_idx)
    postorder(tree, last_node_idx)

    return exterior

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    def is_leaf(node: BinaryTreeNode):
        return node.left is None and node.right is None

    def left_boundary_and_leaves(subtree: BinaryTreeNode, is_boundary: bool):
        if subtree is None:
            return []

        return (([subtree] if is_boundary or is_leaf(subtree) else []) +
                (left_boundary_and_leaves(subtree.left, is_boundary) if subtree.left else
                 left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left)))


    def leaves_and_right_boundary(subtree: BinaryTreeNode, is_boundary: bool):
        if subtree is None:
            return []

        return ((leaves_and_right_boundary(subtree.left, is_boundary and not subtree.right) if subtree.right else
                 leaves_and_right_boundary(subtree.right, is_boundary)) +
                ([subtree] if is_boundary or is_leaf(subtree) else []))

    return ([tree] +
            left_boundary_and_leaves(tree, True) +
            leaves_and_right_boundary(tree, True))\
        if tree else []

def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    #tree = BinaryTreeNode(1)
    #tree.left = BinaryTreeNode(2)
    #tree.right = BinaryTreeNode(3)
    #tree.left.left = BinaryTreeNode(4)
    #tree.left.right = BinaryTreeNode(5)
    #tree.right.left = BinaryTreeNode(6)
    #tree.right.right = BinaryTreeNode(7)

    #result = exterior_binary_tree(tree)
    #print(result)

    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
