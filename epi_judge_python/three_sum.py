from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    p1, p2 = 0, len(A) - 1

    while p1 <= p2:
        num_sum = A[p1] + A[p2]

        if num_sum < t:
            p1 += 1
        elif num_sum > t:
            p2 -= 1
        else:
            return True

    return False


def has_three_sum0(A: List[int], t: int) -> bool:
    for n1 in A:
        for n2 in A:
            for n3 in A:
                if n1 + n2 + n3 == t:
                    return True

    return False


# A = [11, 2, 5, 7, 3]
# t = 21
#
# out_index = 0, out_element = 11, new_t = 10
#
# S = { 8, 5, 3, 7 }
# 2—no, 5—yes, 7—yes, 3—yes
# => *[11, 5, 5], [11, 7, 3], [11, 3, 7]
#
# Note: Returning after first find, so duplicates are ok.
def has_three_sum1(A: List[int], t: int) -> bool:
    for i in range(len(A)):
        partial_t = t - A[i]

        target_difference_set = set()
        for j in range(0, len(A)):
            target_difference_set.add(partial_t - A[j])
            if A[j] in target_difference_set:
                return True

    return False


def has_three_sum2(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        partial_t = t - A[i]

        if has_two_sum(A, partial_t):
            return True

    return False


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()

    return any(has_two_sum(A, t - n) for n in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
