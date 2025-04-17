from typing import Iterator, List

import heapq

from test_framework import generic_test

# Input:
# sequence: Iterator[int], a streamed sequence of ints

# Output:


# Notes / Assumptions:
# - Cannot back up to an earlier value
# - Output median after each new value (running median)

# - Assume have a median
# - If new element is greater than the median, new median will be greater
# - If new element is less than the median, new median will be lesser

# Outline:
# [1, 0, 3, 5, 2, 0, 1]
#   #    C    min    M    max
#   1    1      1    1      1
#   2    0      0    0.5    1
#   3    3      0    1      3
#   4    5      0    2      5
def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap = []
    max_heap = []
    result = []

    for x in sequence:
        smallest_from_larger_half = heapq.heappushpop(min_heap, x)
        heapq.heappush(max_heap, -smallest_from_larger_half)

        if len(max_heap) > len(min_heap):
            largest_from_smaller_half = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, largest_from_smaller_half)

        median = (0.5 * (min_heap[0] + (-max_heap[0]))) if len(min_heap) == len(max_heap) else min_heap[0]
        result.append(median)

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
