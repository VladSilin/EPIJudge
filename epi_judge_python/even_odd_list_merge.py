from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Input:
# L: ListNode, singly-linked list, nodes numbered starting at 0

# Output:
# even_odd_merge: ListNode, a list with all even-numbered nodes followed by odd-numbered nodes

# Notes / Assumptions:
# - The addresses of the nodes are the things we are looking at
# - OR, is it the `data`?

# Example:
# 0 -> 1 -> 2 -> 3 -> N
#
# 0 -> 1 -> 2 -> 3 -> N
# |         ^
# ----------|

# Outline:
# even = node
# odd = even.next
# even.next = odd.next
def even_odd_merge0(L: ListNode) -> Optional[ListNode]:
    even = L

    if even is None or even.next is None:
        return even

    first_even = even
    first_odd = odd = even.next
    prev_even = None
    while even and odd and even.next and odd.next:
        even.next = even.next.next
        prev_even = even
        even = even.next
        odd.next = odd.next.next
        odd = odd.next

    prev_even.next = first_odd

    return first_even

def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(1)

    # TODO: Add to notes (if you wish to alternate an action based on an indicator, set up a list and use the indicator
    #   an index into it rather than using an if-structure)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1

    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
