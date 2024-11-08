import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


#         1
#       /    \
#      2      3
#    /  \   /   \
#   4   *5 6*    7
#
# Note: nodes have parent pointers
def lca0(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.

    node0_parents = set()
    dummy_node0 = parent0 = BinaryTreeNode(0, None, None, node0)
    while parent0:
        parent0 = parent0.parent
        node0_parents.add(parent0)

    dummy_node1 = parent1 = BinaryTreeNode(0, None, None, node1)
    while parent1:
        parent1 = parent1.parent

        if parent1 in node0_parents:
            return parent1

    return None


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node):
        depth = -1
        while node:
            depth += 1
            node = node.parent

        return depth

    depth0, depth1 = get_depth(node0), get_depth(node1)

    # Makes node0 the deeper node in order to simplify the code
    # TODO: Add to notes (strategy to avoid extra variables and confusion in getting the smaller/lareger of 2 values)
    if depth1 > depth0:
        node0, node1 = node1, node0

    # Ascends from the deeper node
    # TODO: Add to notes (strategy to avoid extra variables and confusion in getting the smaller/lareger of 2 values)
    depth_diff = abs(depth0 - depth1)
    # TODO: Add to notes (0 is falsy)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    return node0

@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    node6_data = BinaryTreeNode(7, None, None)
    node5_data = BinaryTreeNode(6, None, None)
    node4_data = BinaryTreeNode(5, None, None)
    node3_data = BinaryTreeNode(4, None, None)
    node2_data = BinaryTreeNode(3, node5_data, node6_data)
    node1_data = BinaryTreeNode(2, node3_data, node4_data)
    node0_data = BinaryTreeNode(1, node1_data, node2_data)

    node1_data.parent = node2_data.parent = node0_data
    node3_data.parent = node4_data.parent = node1_data
    node5_data.parent = node6_data.parent = node2_data

    test_tree = node0_data

    print('test_tree:', test_tree)

    result = lca(node1_data, node5_data)
    print('result:', result)

    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
