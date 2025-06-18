from math import sqrt
from typing import List

import bintrees
from test_framework import generic_test

# Input:
# k: int, how many smallest a + b * sqrt(2) numbers to compute

# Output:
# a_b_sqrt2_numbers: List[float], the k smallest a + b * sqrt(2) numbers

# Notes / Assumptions:

# Examples:

# Outline:


class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def generate_first_k_a_b_sqrt2_0(k: int) -> List[float]:
    for i in range(k):
        print()
        for j in range(k):
            print(j + i * sqrt(2))

    return []


def generate_first_k_a_b_sqrt2_1(k: int) -> List[float]:
    candidates = bintrees.RBTree([(ABSqrt2(0, 0), None)])

    result = []
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)

        candidates[ABSqrt2(next_smallest.a + 1, next_smallest.b)] = None
        candidates[ABSqrt2(next_smallest.a, next_smallest.b + 1)] = None

    return result


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    result = [ABSqrt2(0, 0)]

    i = j = 0
    for _ in range(1, k):
        add_1 = ABSqrt2(result[i].a + 1, result[i].b)
        add_sqrt2 = ABSqrt2(result[j].a, result[j].b + 1)

        result.append(min(add_1, add_sqrt2))

        if add_1.val == result[-1].val:
            i += 1
        if add_sqrt2.val == result[-1].val:
            j += 1

    return [x.val for x in result]


if __name__ == "__main__":
    generate_first_k_a_b_sqrt2(5)
    exit(
        generic_test.generic_test_main(
            "a_b_sqrt2.py", "a_b_sqrt2.tsv", generate_first_k_a_b_sqrt2
        )
    )
