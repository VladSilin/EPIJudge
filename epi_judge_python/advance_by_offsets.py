from typing import List

from test_framework import generic_test

# Inputs:
# A: List[int] (maximum advancements from each position)

# Outputs:
# bool: Is it possible to get to the last index?

# Notes / Assumptions:
# - Array of allowed advancement in one move
# - Can you advance less than the num? Yes

# Example:
# A = [3, 3, 1, 0, 2, 0, 1]

# Brute Force:
# for i, e in enumerate(A):
#     for i in range(e):

def can_reach_end0(A: List[int]) -> bool:
    i = 0
    while A[i] != 0 and i < len(A) - 1:
        max_in_window = max(enumerate(A[i + 1:i + A[i] + 1]), key=lambda p: p[1])

        i = i + max_in_window[0] + 1

    return True if i >= len(A) - 1 else False

# I can always reach the index I'm looking at, since if I couldn't, I would've stopped
# If you're looking at an index, that means it's within reach
# - This way, you're actually considering ALL possibilities of movement
# - i advances by 1 every time, so each possibility is considered but only the one that gets you farthest is taken
#
# Invariants:
# - The index you're looking at is within reach
# - The index within reach only changes if it's an improvement
# - If the end state is reached or no movement is possible, quit
def can_reach_end(A: List[int]) -> bool:
    max_position_so_far, last_index = 0, len(A) - 1

    i = 0
    while i <= max_position_so_far < last_index:
        max_position_so_far = max(i + A[i], max_position_so_far)
        i += 1

    return max_position_so_far >= last_index


if __name__ == '__main__':
    #input = [3, 3, 1, 0, 2, 0, 1]
    #input = [10, 0, 10, 2, 1, 2, 4, 1, 2, 0, 7, 8, 6, 3, 6, 6, 10, 9, 7, 8, 1, 0, 4, 2, 7, 8, 3, 4, 2, 1, 9, 9, 3, 8, 3, 2, 0, 4, 8, 10, 2, 0, 4, 8, 3, 6, 4, 5, 2, 8, 7, 5, 10, 7, 8, 0, 3, 8, 1, 8, 8, 10, 6, 8, 7, 3, 4, 8, 5, 10, 9, 5, 7, 8, 1, 8, 7, 9, 8, 6, 4, 0, 1, 3, 8, 3, 10, 1, 6, 7, 6, 4, 4, 10, 2, 3, 1, 2, 1, 8, 1, 4, 0, 3, 10, 8, 1, 1, 7, 3, 3, 8, 1, 0, 5, 6, 10, 3, 0, 5, 7, 3, 9, 9, 2, 5, 1, 1, 5, 4, 3, 10, 10, 0, 7, 7, 2, 3, 4, 3, 7, 8, 0, 1, 10, 9, 6, 9, 9, 6, 2, 2, 0, 9, 7, 8, 8, 4, 1, 1, 9, 4, 8, 6, 5, 6, 10, 5, 4, 6, 9, 3, 10, 9, 4, 5, 6, 6, 8, 3, 2, 5, 4, 8, 0, 1, 3, 1, 0, 1, 0, 3, 7, 7, 8, 1, 9, 4, 7, 9, 1, 5, 9, 4, 0, 2, 2, 2, 7, 8, 8, 3, 2, 10, 5, 3, 0, 10, 7, 5, 8, 8, 10, 9, 1, 9, 8, 10, 7, 9, 4, 10, 1, 3, 3, 2, 1, 9, 9, 7, 10, 4, 7, 10, 8, 8, 7, 2, 2, 5, 7, 4, 1, 4, 3, 10, 3, 7, 5, 1, 0, 2, 6, 9, 0, 2, 3, 5, 1, 4, 6, 0, 4, 4, 7, 0, 0, 1, 2, 0, 1, 2, 9, 1, 0, 2, 6, 10, 10, 0, 2, 9, 7, 10, 0, 1, 10, 0, 4, 2, 7, 10, 3, 5, 2, 4, 7, 3, 0, 3, 8, 9, 6, 3, 3, 6, 3, 4, 9, 7, 9, 0, 4, 4, 6, 4, 6, 2, 2, 2, 8, 6, 6, 6, 9, 3, 7, 7, 1, 0, 1, 6, 9, 2, 3, 6, 10, 0, 0, 0, 3, 6, 8, 7, 0, 4, 0, 5, 7, 2, 3, 5, 8, 0, 4, 6, 9, 8, 6, 10, 10, 9, 6, 1, 0, 5, 4, 8, 8, 1, 7, 1, 5, 9, 8, 3, 2, 3, 3, 2, 3, 9, 3, 8, 4, 3, 4, 1, 0, 7, 4, 1, 4, 8, 4, 5, 10, 10, 0, 4, 7, 8, 8, 8, 5, 4, 10]
    #print(input[185:200])
    #result = can_reach_end(input)

    #print(result)
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
