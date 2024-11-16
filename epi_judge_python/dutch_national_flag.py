import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# Inputs:
# - array, A: List[int]
# - pivot, i: int
#
# Result:
# - (in-place) Partition s.t. elements less than, then equal to, then greater than the pivot
#
# Notes:
# - An array reordered s.t. 3 paritions
#     - Elems. less than the pivot
#     - Elems. equal to the pivot
#     - Elems. greater than the pivot
#
# Example:
# A = [0, 1, 2, 0, 2, 1, 1]
# i = 3, A[i] = 0
#
# Put pivot at the end:
# A = [0, 2, 2, 1, 1, 1, 0]
#      l
#      m
#         h
# [l, m, m, l, l, l, h, h, h, p]
#                    l
#                 h
# TODO: Add to notes (technique for partitioning problems, categorize elements rather than listing explicitly)
# Start:
# [l, l, m, m, l, l, h, h, h, p]
#
# [l, l, l, l, m, m, p, h, h, h]
#           d        l
#                 m
#                 h
#
# [l, l, l, l, l, m, m, h, h, h, h, p]
#              d
#                       l
#                    h
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    if len(A) == 0:
        return

    pivot = A[pivot_index]

    # Swap pivot with last element
    A[pivot_index], A[-1] = A[-1], A[pivot_index]

    l, d, h = 0, -1, len(A) - 2

    while l <= h:
        if A[l] > pivot:
            A[l], A[h] = A[h], A[l]
            h -= 1
        elif A[l] < pivot:
            # In this case, no middle partition yet exists
            if d == -1:
                l += 1
            else:
                A[l], A[d] = A[d], A[l]
                d += 1
                l += 1
        # This is the "equal to pivot" case
        else:
            if d == -1:
                d = l
                l += 1
            else:
                l += 1

    # Put the pivot back by swapping it with the "high" pointer
    # This works due to the '<=' loop condition above
    A[-1], A[l] = A[l], A[-1]


# Potentially correct algorithm for a quicksort partition step?
def quicksort_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    # Swap pivot with last element
    A[pivot_index], A[-1] = A[-1], A[pivot_index]

    l, m, h = 0, 0, len(A) - 2

    while l <= h:
        if A[l] > pivot:
            A[l], A[h] = A[h], A[l]
            h -= 1
        elif A[l] < pivot:
            l += 1

    # Put the pivot back by swapping it with the "high" pointer
    # Note the '+ 1' due to the loop condition above
    A[-1], A[h + 1] = A[h + 1], A[-1]

def dutch_flag_partition0(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    A[pivot_index], A[len(A) - 1] = A[len(A) - 1], A[pivot_index]

    # The last element strictly smaller than the pivot
    i = -1
    # The last element which is strictly equal to the pivot
    k = -1

    # The index which will "find" the smaller elements
    j = 0

    # TODO: Add to notes (Useful approach to stepping through array problems)
    # pivot = 2
    #  [1, 2, 1, 2, 3]
    #   i
    # k
    #      j
    while j < len(A) - 1:
        # The element is strictly LESS than the pivot
        if A[j] < pivot:
            # If an "equal" partition exists, 2 chained swaps
            if k > -1:
                A[j], A[k + 1] = A[k + 1], A[j]
                A[i + 1], A[k + 1] = A[k + 1], A[i + 1]
                i += 1
                k += 1
            # Otherwise, do the normal partition action
            else:
                A[j], A[i + 1] = A[i + 1], A[j]
                i += 1
        # The element is strictly EQUAL to the pivot
        elif A[j] == pivot:
            # If a "less" partition already exists but not yet an "equal" one, then create an "equal" one at the end
            # of the "less" one.
            if i > -1 and k < 0:
                A[j], A[i + 1] = A[i + 1], A[j]
                k = i + 1
            else:
                A[j], A[k + 1] = A[k + 1], A[j]
                k += 1

        j += 1

    # Move the pivot from the end of the list to the correct place
    if k > -1:
        A[len(A) - 1], A[k + 1] = A[k + 1], A[len(A) - 1]
    else:
        A[len(A) - 1], A[i + 1] = A[i + 1], A[len(A) - 1]

    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    #test_list = [1, 0, 0, 0, 0, 1, 1, 0, 2, 2, 1, 1, 3, 4, -1, -2, 1]
    #test_list = [-1, -2, -3, 2, 0, 1]
    #test_list = [2, 3, 2, 5, 1, 2, 3, 2, 2, 2]
    #dutch_flag_partition(9, test_list)
    #print(test_list)
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
