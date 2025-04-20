from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Input:
# L: ListNode, head of linked list
# k: int, which node from last to return

# Output:
# kth_last_node: ListNode, the kth last node of the list

# Notes / Assumptions:
# - Cannot use more than a few words of extra storage

# Example:

# Outline:

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)

    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next

    second.next = second.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
