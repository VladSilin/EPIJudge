from typing import List

from test_framework import generic_test

# Input:
# grid: List[List[int]], a 2D array of integers
# pattern: List[int], a 1D array of integers

# Output:
# does_pattern_occur: bool, can the pattern be formed by traversing the 2D array left, right, up, or down in sequence

# Notes / Assumptions:
# - Acceptable to visit an entry more than once
#   - "Going back" implies a duplicate entry (a pattern is NOT a set)

# Examples:
# [
#    [1, 2, 3],
#    [3, 4, 5],
#    [5, 6, 7],
# ]
# [1, 3, 4, 6]

# At (0, 0), cur_pattern_element = 1; is_valid_path?; actions: go left, go right, go up, go down
#   go left; is_valid_path?; actions: go left, go right, go up, go down
#      go left; is_valid_path? actions: ...
#   go right; ...

# Outline:
# grid[i][j], cur_pattern_element = pattern[k]; is_valid_path = grid[i][j] == pattern[k]; actions: j -= 1, j += 1, i -= 1, i += 1
#   j - 1: ...


def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
    previous_attempts = set()

    def does_current_elem_satisfy_current_path_elem(
        i: int, j: int, current_pattern_element_idx: int
    ):
        if len(pattern) == current_pattern_element_idx:
            return True

        if (
            (0 <= i < len(grid) and 0 <= j < len(grid[i]))
            and grid[i][j] == pattern[current_pattern_element_idx]
            and (i, j, current_pattern_element_idx) not in previous_attempts
            # TODO: Add to notes (traverse in any direction from a coordinate)
            and any(
                does_current_elem_satisfy_current_path_elem(
                    i + a, j + b, current_pattern_element_idx + 1
                )
                for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1))
            )
        ):
            return True

        # This case is where the current elem + pattern elem are not satisfactory
        previous_attempts.add((i, j, current_pattern_element_idx))
        return False

    return any(
        does_current_elem_satisfy_current_path_elem(x, y, 0)
        for x in range(len(grid))
        for y in range(len(grid[x]))
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_in_matrix.py",
            "is_string_in_matrix.tsv",
            is_pattern_contained_in_grid,
        )
    )
