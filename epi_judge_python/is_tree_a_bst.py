from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    previous_value = float('-inf')

    def _is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
        if not tree:
            return True

        is_left_bst = _is_binary_tree_bst(tree.left)

        nonlocal previous_value
        if previous_value > tree.data:
            return False
        previous_value = tree.data
        print(tree.data)

        is_right_bst = _is_binary_tree_bst(tree.right)

        return is_left_bst and is_right_bst

    return _is_binary_tree_bst(tree)


if __name__ == '__main__':
    # tree = BinaryTreeNode(-107, BinaryTreeNode(-115, None, BinaryTreeNode(-112, None, BinaryTreeNode(-107))),
    #                       BinaryTreeNode(-104, None, BinaryTreeNode(-104)))
    # print(is_binary_tree_bst(tree))
    # [-107, -115, -104, null, -112, null, -104, null, -107]
    # print(tree)
    #              -22
    #            /     \
    #          -24     -17
    #          /  \    /  \
    #            -23 -24

    # tree = BinaryTreeNode(-22, BinaryTreeNode(-24, None, BinaryTreeNode(-23)), BinaryTreeNode(-17, BinaryTreeNode(-24)))
    # [-22, -24, -17, null, -23, -24]
    # print(tree)
    # print(is_binary_tree_bst(tree))
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
