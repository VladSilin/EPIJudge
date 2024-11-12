from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# N -> a -> b -> c -> d -> N
# p    c    t

# N <- a    b -> c -> d -> N
#      p    c    t

# N <- a <- b    c -> d -> N
#           p    c    t

# N <- a <- b <- c <- d    N
#                     p    c

def reverse_list(L: ListNode):
    prev = None
    cur = L

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO: Add to notes (use a dummy head (sentinel) to avoid having to check for empty nodes)
    dummy_head = pre_sublist_head = ListNode(0, L)
    # Check if need to start at 2 without dummy head? Yes
    for _ in range(1, start):
        pre_sublist_head = pre_sublist_head.next

    # NOTE: pre_sublist_head ends up 1 node earlier than the actual sublist head
    # Then, we start the iteration at the actual sublist head
    old_head = pre_sublist_head.next
    for _ in range(finish - start):
        temp = old_head.next

        old_head.next = temp.next
        temp.next = pre_sublist_head.next
        pre_sublist_head.next = temp

    # Basically, we're removing each element after the "old_head"
    # and putting it after the pre_sublist_head
    # 1 -> 2 -> 3 -> 4 -> 5
    #      p    c    t
    #
    #      pre_sublist_head.next = temp (put the thing that used to be after the old head, after the pre_sublist_head)
    #      -----------
    #      |         v
    # 1 -> 2    3 <- 4    5           [3 <- 4]: temp.next = pre_sublist_head.next
    #           |         ^
    #           -----------
    #           old_head.next = temp.next
    #
    # 1 -> 2 -> 4 -> 3 -> 5
    #      p         c    t

    # NOTE: In the case that the first index is part of the sublist, the L will no longer point to the correct
    # starting node and thus dummy_head.next must be used
    return dummy_head.next


def reverse_sublist0(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # Save the splice_start node
    # Save the splice_finish node
    # Save the node after the splice start (this will be the "new_tail")
    # Reverse the list segment
    # Set splice_start.next to head of reversed segment
    # Set new_tail.next to splice_finish

    if start < 1:
        return L

    index = 1
    prev = None
    cur = L

    splice_start = None
    splice_finish = None
    new_tail = None

    while cur:
        if index == start:
            splice_start = prev
            new_tail = cur

        if index == finish:
            splice_finish = cur.next
            cur.next = None
            break

        index += 1

        prev = cur
        cur = cur.next

    new_head = reverse_list(new_tail)

    if splice_start:
        splice_start.next = new_head
    if splice_finish and new_tail:
        new_tail.next = splice_finish

    return new_head if not splice_start else L


if __name__ == '__main__':
    test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    # print(reverse_sublist(test_list, 3, 5))
    #print(reverse_sublist(test_list, 4, 5))
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
