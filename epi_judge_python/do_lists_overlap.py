import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:
# l0: ListNode, head of a linked list
# l1: ListNode, head of another linked list

# Output
# shared_node: ListNode, the first node common to both lists

# Notes / Assumptions:

# Example:
# - Check if the next node of both lists is the
# 1 -> N
# 1 -> N

# 1 -> 2 -> N
#      ^
# 1 ---|

# Outline:

def overlapping_lists0(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    if l0 is None or l1 is None:
        return None
    # TODO - you fill in here.
    l0_nodes = set()
    while l0 is not None:
        l0_nodes.add(id(l0))
        l0 = l0.next

    while l1 is not None:
        if id(l1) in l0_nodes:
            return l1

        l1 = l1.next

    return None

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    def length(L):
        length = 0
        while L is not None:
            length += 1
            L = L.next

        return length

    l0_len, l1_len = length(l0), length(l1)
    if l0_len > l1_len:
        # l1 is always the longer list
        l0, l1 = l1, l0

    for _ in range(abs(l0_len - l1_len)):
        l1 = l1.next

    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next

    return l0


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
