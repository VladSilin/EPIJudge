import functools
from collections.abc import Callable
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections

# Input:
# - Bin. tree, tree: BinaryTreeNode; No parent ref.

# Output:
# - lca BinaryTreeNode: Lowest common ancestor, common ancestor of both nodes furthest from the root

# Notes / Assumptions:
# - Will need to keep state
# - Search for the first node, keeping track of the path taken (set of nodes), O(N)
# - Search for the 2nd node, keeping track of the path taken (stack), O(N)
# - Pop items off the 2nd node's stack and check if each is in the first path set O(N)
# - Overall O(N)

# Example:


def lca0(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    def search(t: BinaryTreeNode, n: BinaryTreeNode):
        q = [[t]]
        while q:
            cur_path = q.pop(0)
            cur = cur_path[len(cur_path) - 1]

            if cur == n:
                return cur_path

            if cur.left:
                q.append(cur_path + [cur.left])
            if cur.right:
                q.append(cur_path + [cur.right])

        return []

    path0 = search(tree, node0)
    # TODO: Add to notes (worst case, use id() to "hash" unhashable custom classes)
    node_set = set([id(x) for x in path0])

    path1 = search(tree, node1)
    node_stack = path1

    cur_node = node_stack.pop()
    while id(cur_node) not in node_set:
        cur_node = node_stack.pop()

    return cur_node


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(root, n0, n1):
        if not root:
            return Status(0, None)

        left_result = lca_helper(root.left, n0, n1)
        if left_result.num_target_nodes == 2:
            return left_result

        right_result = lca_helper(root.right, n0, n1)
        if right_result.num_target_nodes == 2:
            return right_result

        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes + int(root is n0) + int(root is n1)
        )

        return Status(num_target_nodes, root if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
