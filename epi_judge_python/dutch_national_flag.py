import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
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
    # test_list = [0, 0, 0, 0, 1, 1, 2, 1, 1]
    # dutch_flag_partition(4, test_list)
    # print(test_list)
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
