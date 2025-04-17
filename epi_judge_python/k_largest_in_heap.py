from shutil import which
from typing import List

import heapq

from test_framework import generic_test, test_utils


# Input:
# A: List[int], max heap rep. as a list
# k: int, number of largest elements to return

# Output:
# result: List[int], the k largest elements in the heap

# Example:
# h = [37,    29,  19,    22,   12,     18,   5]

# Notes / Assumptions:

# Outline:
def k_largest_in_binary_heap0(A: List[int], k: int) -> List[int]:
    max_heap = []
    result = []

    i = 0
    count = 0
    which_child = 0
    while i < len(A):
        if count < k:
            heapq.heappush(max_heap, -A[i])
            count += 1
        else:
            largest = -heapq.heappushpop(max_heap, -A[i])
            result.append(largest)

        i = (i * 2 + 1) if which_child == 0 else i + 1
        # TODO: Add to notes, flipping a bit
        which_child = 1 - which_child

    while max_heap:
        result.append(-heapq.heappop(max_heap))

    return result[:k]

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []

    candidate_max_heap = [(-A[0], 0)]
    result = []

    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        cur_max = -heapq.heappop(candidate_max_heap)[0]
        result.append(cur_max)

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))

        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
