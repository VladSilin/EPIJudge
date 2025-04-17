import itertools
from collections import defaultdict
from typing import Iterator

from test_framework import generic_test


# Input:
# stream: Iterator[str], sequence of strings

# Output:
# majority_e: The element occurring the most number of times

# Notes / Assumptions:
# - More than half the strings are repetitions (majority element)
#   - Positions unknown
# - There exists some subset of 'stream' of size len(stream) / 2 which is all 's', where 's' is some string

# Example:
# [b, a, c, a, a, b, a, a, c, a]

# Brute Force Outline:
# - Iterate through the entire stream
# - Store a running count of occurrences in a hashmap
def majority_search0(stream: Iterator[str]) -> str:
    s = ''
    s_to_count = defaultdict(lambda: 0)
    total = 0
    while True:
        try:
            cur = next(stream)
            s_to_count[cur] = s_to_count[cur] + 1
            total += 1

            if s_to_count[cur] / total > 0.5:
                s = cur
        except StopIteration:
            break

    return s

def majority_search(stream: Iterator[str]) -> str:
    candidate, candidate_count = None, 0

    for it in stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1

    return candidate

def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
