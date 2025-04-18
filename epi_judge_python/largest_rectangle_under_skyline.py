from typing import List

from test_framework import generic_test


# Input:
# heights: List[int], heights of buildings

# Output:
# max_area: int, area of largest rectangle

# Notes / Assumptions:

# Example:

# Outline:
def calculate_largest_rectangle(heights: List[int]) -> int:
    pillar_indices, max_rectangle_area = [], 0

    for i, h in enumerate(heights + [0]):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1

            max_rectangle_area = max(max_rectangle_area, height * width)

        pillar_indices.append(i)

    return max_rectangle_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
