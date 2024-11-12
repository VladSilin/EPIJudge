from typing import Optional

from list_node import ListNode
from test_framework import generic_test

'''
NOTE: When representing a list as a node, this node points to the head and should remain pointing to the head.

A SEPARATE pointer should always be created which can be updated to iterate through the list.
'''


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # L1: 1 -> 3 -> 4 -> 7 -> 9
    #          p
    # L2: 1 -> 2 -> 8 -> 11 -> 13
    #          q

    output_list_dummy_head = output_pointer = ListNode()
    p1, p2 = L1, L2

    while p1 and p2:
        if p1.data <= p2.data:
            output_pointer.next = ListNode(p1.data)
            output_pointer = output_pointer.next

            p1 = p1.next
        else:
            output_pointer.next = ListNode(p2.data)
            output_pointer = output_pointer.next

            p2 = p2.next

    output_pointer.next = p1 or p2

    return output_list_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
