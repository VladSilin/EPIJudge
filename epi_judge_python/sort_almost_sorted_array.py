import heapq
from typing import Iterator, List

import itertools

from setuptools.dist import sequence

from test_framework import generic_test

# Inputs:
# sequence: Iterator[int], a long sequence of numbers
# k: The largest distance a num. is away from its sorted position

# Outputs:
# result: List[int], a sorted list

# Notes / Assumptions:

# Brute Force:
# - Perform an insertion sort into a new array (O(n^2))
# -
def sort_approximately_sorted_array0(sequence: Iterator[int],
                                    k: int) -> List[int]:
    result = []
    min_heap = []

    count = 0
    while True:
        try:
            elem = next(sequence)
            if count <= k:
                heapq.heappush(min_heap, elem)
                k += 1
            else:
                smallest = heapq.heappushpop(min_heap, elem)
                result.append(smallest)
        except StopIteration:
            break

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    result = []
    min_heap = []

    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
