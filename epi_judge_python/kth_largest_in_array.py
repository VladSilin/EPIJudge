from typing import List

from test_framework import generic_test

import operator
import random

# A = [3, 1, -1, 2]
# pivot_i = 0

# A = [1, -1, 1, 3]

# XXXXXXyZZZZZZZ
# AAAAAAAAAAA

# BBBBBBBZZZZZZZ
# AAAAAAAAAAA

# BBBBBBBBZZZZyZ
# AAAAAAAAAAA

# BBBBBBBBZZZZBB
# AAAAAAAAAAA

# BBBBBBBBZZyZBB
# AAAAAAAAAAA


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def find_kth(comp):
        # [3, 1, -1, 2]
        #     p

        # [3, 2, -1, 1]
        #            p
        #        l
        #        i
        def partition_around_pivot(start, end, pivot_index):
            pivot_value = A[pivot_index]

            # TODO: Add to notes (partition algo)
            # Swap pivot element and last element to get the pivot out of the way
            A[pivot_index], A[end] = A[end], A[pivot_index]

            # This index will keep track of the index after the last
            # already partitioned index (the i will go search for other greater than elements)
            after_processed_index = start
            for i in range(start, end):
                if comp(A[i], pivot_value):
                    A[after_processed_index], A[i] = A[i], A[after_processed_index]
                    after_processed_index += 1

            # Put back the pivot where it belongs (at the "after_processed_index",
            # Since this then guarantees that all elements to the right of the new pivot
            # are less than
            A[end], A[after_processed_index] = A[after_processed_index], A[end]
            new_pivot_index = after_processed_index

            return new_pivot_index

        start, end = 0, len(A) - 1
        while start <= end:
            pivot_index = random.randint(start, end)
            new_pivot_index = partition_around_pivot(start, end, pivot_index)

            if new_pivot_index == k - 1:
                return A[new_pivot_index]
            elif new_pivot_index > k - 1:
                end = new_pivot_index - 1
            elif new_pivot_index < k - 1:
                start = new_pivot_index + 1

    return find_kth(operator.gt)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
