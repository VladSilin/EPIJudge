import functools
from typing import List

from epi_judge_python_solutions.remove_duplicates_from_sorted_list import remove_duplicates
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Input:
# A: List[int] (sorted list of integers)

# Output:
# numValidElements: int (result after removing duplicated elements)

# Notes / Assumptions:
# - Since the array is sorted, duplicate elements are consecutive

# Example
# A = [2, 3, 5, 5, 7, 11, 11, 11, 13, 14, 15]
# A = [2, 3, 5, 7, 11, 13, 14, 15, 13, 14, 15, 15]
#      i
#      r
# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    i, r = 0, 0
    while r < len(A) - 1:
        # TODO: Add to notes (use an inner loop as an abstraction for incrementing more than once)
        while A[r] == A[i] and r < len(A) - 1:
            r += 1

        if A[i] != A[r]:
            A[i + 1] = A[r]
            i += 1

    return i + 1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    #test = [1, 2, 3, 5, 5, 7, 11, 11, 11, 13, 14, 15, 15, 15]
    #test = [1]
    #test = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8]
    #result = delete_duplicates(test)
    #print(test)
    #print('' if len(test) == 0 else ((' ' * (len(''.join([c for c in str(test[:result]) if c not in '[]'])) - len(str(test[result - 1])) + 1)) + '^'))
    #print('result', result)

    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
