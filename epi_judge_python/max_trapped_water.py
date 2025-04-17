from typing import List

from test_framework import generic_test

# Input:
# heights: List[int], list of nums. rep. the height of the wall at each index

# Output:
# water: int, max amount of water trapped by 2 lines

# Notes / Assumptions:
# - Find the longest 2 lines from either end
# - Multiply the length of the shorter one by the diff. b/w the 2 indices

# Example:

# Outline:
def get_max_trapped_water(heights: List[int]) -> int:
    get_water = lambda l, r, li, ri: min(l, r) * (ri - li)

    max_water = 0
    i, j = 0, len(heights) - 1
    while i < j:
        max_water = max(max_water, get_water(heights[i], heights[j], i, j))

        if heights[i] > heights[j]:
            j -= 1
        else:
            i += 1

    return max_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
