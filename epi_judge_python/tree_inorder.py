from typing import List
from collections import namedtuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Input:
# - tree: BinaryTreeNode, a tree with parent refs

# Output:
# - List[int]: A list of nodes from in-order traversal

# Notes / Assumptions:
# - Non-recursive
# - O(1) space (no stack?)

# Example:

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    StackFrame = namedtuple('StackFrame', ('node', 'ops'))

    result = []
    stack = [StackFrame(tree, ['left', 'visit', 'right'])]

    while stack:
        frame = stack[len(stack) - 1]

        node = frame.node
        ops = frame.ops

        if not node or not ops:
            stack.pop()
            continue

        op = ops.pop(0)

        if op == 'left':
            left_node = node.left
            if left_node:
                stack.append(StackFrame(left_node, ['left', 'visit', 'right']))
        elif op == 'visit':
            result.append(node.data)
        elif op == 'right':
            right_node = node.right
            if right_node:
                stack.append(StackFrame(right_node, ['left', 'visit', 'right']))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
