from typing import List

from test_framework import generic_test

import heapq
from collections import namedtuple


def merge_sorted_arrays_basic(sorted_arrays: List[List[int]]) -> List[int]:
    result = []

    CurElementToWhichArray = namedtuple('CurElementToWhichArray', ('cur_element', 'which_array'))
    min_heap = [CurElementToWhichArray(cur_element=sorted_array[1][0], which_array=sorted_array[0]) for sorted_array
                in enumerate(sorted_arrays) if sorted_array[1]]

    heapq.heapify(min_heap)

    while any(sorted_arrays):
        # Get the minimum element and the array it belongs to
        min_element, min_element_array_index = heapq.heappop(min_heap)

        # Append the minimum to the result
        result.append(min_element)
        # Get rid of this minimum element from the corresponding array
        sorted_arrays[min_element_array_index].pop(0)

        if sorted_arrays[min_element_array_index]:
            heapq.heappush(min_heap, CurElementToWhichArray(cur_element=sorted_arrays[min_element_array_index][0],
                                                            which_array=min_element_array_index))

    return result


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result = []

    # NOTE: Since arrays in Python are compared lexicographically, can just store all arrays themselves in the heap!
    # (Leads to an elegant algorithm)
    heapq.heapify(sorted_arrays)

    while any(sorted_arrays):
        # Get the minimum element array
        min_element_array = heapq.heappop(sorted_arrays)

        # Append the minimum to the result
        if min_element_array:
            result.append(min_element_array.pop(0))
            heapq.heappush(sorted_arrays, min_element_array)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
