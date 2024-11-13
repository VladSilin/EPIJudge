from typing import List

from test_framework import generic_test


# 1st array has enough space to store 2nd array
# A = [5, 13, 17, _, _, _, _, _]
# B = [3, 7, 11, 19].
#
# A = [_, 3, 5, 7, 11, 13, 17, 19]
#      i
#      w
# B = [_, _, _, _]
#      j

# A = [-1, 0, 0, 0, 0]
# B = [-3, -1, 0, 3]
#
# A = [0, 0, -1, 0, 3]
#    i    w
# B = [-3, -1, 0, 3]
#          j
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    i, j = m - 1, n - 1

    # TODO: Figure out the textbook solution (equivalent but different)
    # TODO: Add to notes (strategy: traverse arrays from the end)
    #
    # TODO: Add to notes (strategy: when dealing with "arrays",
    #  think of swapping "empty" elements first rather than replacing)
    #
    # TODO: Add to notes (traverse list backwards using range())
    for write_index in range((m + n) - 1, -1, -1):
        # If not finished with list A and (finished with list B or A element is bigger than B element)
        if i != -1 and (j == -1 or A[i] >= B[j]):
            A[write_index] = A[i]
            i -= 1
        # If not finished with list B and (finished with list A or B element is bigger than A element)
        elif j != -1 and (i == -1 or A[i] < B[j]):
            A[write_index] = B[j]
            j -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
