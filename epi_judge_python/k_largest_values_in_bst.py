from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO: Add to notes (ascending order in-order traversal)
    def _in_order_reverse(_tree: BstNode, _storage: [BstNode]):
        if not _tree or len(_storage) >= k:
            return

        _in_order_reverse(_tree.right, _storage)
        if len(_storage) < k:
            storage.append(_tree.data)
            _in_order_reverse(_tree.left, _storage)

    storage = []
    _in_order_reverse(tree, storage)

    return storage


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
