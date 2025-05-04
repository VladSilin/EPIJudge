import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple(
    "DuplicateAndMissing", ("duplicate", "missing")
)


# Input:
# A: List[int]

# Output:
# duplicate: int
# missing: int

# Notes / Assumptions:

# Example:

# Outline:


def find_duplicate_missing0(A: List[int]) -> DuplicateAndMissing:
    seen_elements = set()

    duplicate = -1
    missing = -1
    for x in A:
        if x in seen_elements:
            duplicate = x
            continue

        seen_elements.add(x)

    for i in range(len(A)):
        if i not in seen_elements:
            missing = i

    return DuplicateAndMissing(duplicate, missing)


def find_duplicate_missing1(A: List[int]) -> DuplicateAndMissing:
    A.sort()

    duplicate = -1
    missing = -1

    for i in range(len(A)):
        if i > 0 and A[i] == A[i - 1]:
            duplicate = A[i]
        elif i > 0 and A[i] > A[i - 1] + 1:
            missing = A[i - 1] + 1

    # Handle the case where the missing number is the last one (n - 1)
    if missing == -1:
        if A[-1] != len(A) - 1:
            missing = len(A) - 1
        else:
            missing = len(A)

    return DuplicateAndMissing(duplicate, missing)


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    # Compute the XOR of all numbers from 0 to |A| - 1 and all entries in A
    miss_XOR_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)

    # We need to find a bit that's set to 1 in miss_XOR_dup. Such a bit must
    # exist if there is a single missing number and a single duplicated number
    # in A.
    #
    # The bit-fiddling assignment below sets all of the bits in differ_bit
    # to 0 except for the least significant bit in miss_XOR_dup that's 1.
    differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0
    for i, a in enumerate(A):
        # Focus on entries and numbers in which the differ_bit-th bit is 1
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    # miss_or_dup is either the missing value or the duplicated entry.
    if miss_or_dup in A:
        # miss_or_dup is the duplicate.
        return DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_XOR_dup)
    # miss_or_dup is the missing value.
    return DuplicateAndMissing(miss_or_dup ^ miss_XOR_dup, miss_or_dup)


def res_printer(prop, value):
    def fmt(x):
        return "duplicate: {}, missing: {}".format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED, PropertyName.RESULT) else value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            "find_missing_and_duplicate.tsv",
            find_duplicate_missing,
            res_printer=res_printer,
        )
    )
