from typing import List

from test_framework import generic_test


# [-2, 1, 2, 4, 7, 11]
# t = 6
#
# Start pointers p1 at 0 and p2 at len(A) - 1
#
# If p1 + p2 < t, then we need a larger sum (so the correct number cannot be p1 or anything to the left).
# Thus, advance p1.
#
# If p1 + p2 > t, then we need a lesser sum (so the correct number cannot be p2 or anything to the right).
# Thus, advance p2 (to the left).


def has_two_sum0(A: List[int], t: int) -> bool:
    difference_table = set()

    for num in A:
        difference_table.add(t - num)
        if num in difference_table:
            return True

    return False


def has_two_sum(A: List[int], t: int) -> bool:
    i, j = 0, len(A) - 1

    while i <= j:
        num_sum = A[i] + A[j]

        if num_sum < t:
            i += 1
        elif num_sum > t:
            j -= 1
        else:
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
