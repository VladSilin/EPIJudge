from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple
import test_framework.binary_tree_utils as tree_utils


def __height(tree: BinaryTreeNode) -> int:
    if tree is None:
        return 0

    return max(__height(tree.left), __height(tree.right)) + 1


# Height-balanced: For EACH node in the tree, node.height(left) - node.height(right) <= 1
def __is_balanced(tree: BinaryTreeNode) -> bool:
    if tree is None:
        return True

    left_height = __height(tree.left)
    right_height = __height(tree.right)
    is_balanced = abs(left_height - right_height) <= 1

    return is_balanced and __is_balanced(tree.left) and __is_balanced(tree.right)


def __is_balanced_reference(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('is_balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(is_balanced=True, height=-1)

        left_result = check_balanced(tree.left)
        if not left_result.is_balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result.is_balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1

        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).is_balanced


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return __is_balanced_reference(tree)
    # return __is_balanced(tree)


#       1
#      / \
#     3   7
#    /
#   4
#  /
# 5
#
#        4
#     /     \
#   -4      -2
#   / \     / \
#      7   1
#     / \
#        6
if __name__ == '__main__':
    # tree = BinaryTreeNode(1, BinaryTreeNode(3, BinaryTreeNode(4, BinaryTreeNode(5))), BinaryTreeNode(7))
    # print(str(tree))
    # print(__is_balanced(tree))

    # test_tree = BinaryTreeNode(4, BinaryTreeNode(-4, None, BinaryTreeNode(7, None, BinaryTreeNode(6))),
    #                            BinaryTreeNode(-2, BinaryTreeNode(1), None))
    #     test_tree = BinaryTreeNode(-4, None, BinaryTreeNode(7, None, BinaryTreeNode(6)))
    # print(str(test_tree))

    # print(__is_balanced(test_tree))
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
