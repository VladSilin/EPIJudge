from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

#   314
#   /  \
#  6    6
# / \  / \
# 1 3  4 7
#
# [[314]]


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []

    result = []
    visit_queue = [tree]

    while visit_queue:
        result.append([node.data for node in visit_queue])

        # NOTE: Equivalent imperative version (note the similar order of nested for's)
        # new_visit_queue = []
        # for node_to_visit in visit_queue:
        #     for child in (node_to_visit.left, node_to_visit.right):
        #         if child:
        #             new_visit_queue.append(child)
        # visit_queue = new_visit_queue

        # NOTE: Basically "extracting" what would/could be in the "kernel" of the nested loops to the
        # place where "child" is
        visit_queue = [child for node_to_visit in visit_queue
                       for child in (node_to_visit.left, node_to_visit.right) if child]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
