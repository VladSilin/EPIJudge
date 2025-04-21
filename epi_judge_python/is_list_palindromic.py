from list_node import ListNode
from test_framework import generic_test

# Input:
# L: ListNode, a singly linked list head

# Output:
# is_palindromic: bool, is the list palindromic?

# Notes / Assumptions:
# - For an array, can iterate from both ends and compare elements
# - For a linked list, can only iterate one way

# - Could find the length of the list by iterating once
# - Trivial:
#   - Put the whole thing in a Python list, then test palindromicity of the list
# - Challenge:
#   - Do this with no additional space
#   - Iterate once to find length
#   - Iterate half while reversing the list
#   - Iterate half while comparing, break if node not equal
#   - Special case? Odd vs even # nodes

# Example:

# Outline:

def is_linked_list_a_palindrome0(L: ListNode) -> bool:
    length = 0
    cur = L
    while cur:
        cur = cur.next
        length += 1

    # Reverse half the list
    half = length // 2
    prev = None
    cur = L
    for _ in range(half):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    # Check for odd number of nodes
    if length % 2 > 0:
        cur = cur.next

    h1, h2 = prev, cur
    while h1 and h2:
        if h1.data != h2.data:
            return False

        h1, h2 = h1.next, h2.next

    return True

def reverse_list(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fast = L
    # TODO: Add to notes (approach to get a pointer to the 2nd half of a linked list)
    while fast and fast.next:
        fast, slow, = fast.next.next, slow.next

    first_half_iter, second_half_iter = L, reverse_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False

        second_half_iter, first_half_iter = second_half_iter.next, first_half_iter.next

    return True


if __name__ == '__main__':
    #n = ListNode(0, ListNode(1, ListNode(1, ListNode(0, ListNode(0)))))

    #print(is_linked_list_a_palindrome(n))
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
