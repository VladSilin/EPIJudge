import itertools
from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

# Input:
# stream: Iterator[int], a stream of 32-bit IP addresses

# Output:
# missing_ip: int, the IP address that is not in the stream

# Notes / Assumptions:
# - Limited RAM implies that only batches (incomplete) of IPs are available
# - Decision: Best way to store intermediary "batches" of IPs

# Example:

# Outline:


def find_missing_element0(stream: Iterator[int]) -> int:
    SIZE = 32
    MASK = 0
    count_1, count_0 = 0, 0
    for i in range(SIZE - 1, -1, -1):
        bit_shift = i
        stream, stream_copy = itertools.tee(stream)
        for ip in stream_copy:
            shifted = ip >> bit_shift

            if shifted == 1:
                count_1 += 1
            elif shifted == 0:
                count_0 += 1

        MASK = MASK | 1 << bit_shift if count_1 < 2**31 else MASK

    return 0


def find_missing_element(stream: Iterator[int]) -> int:
    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET

    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter) if c < BUCKET_CAPACITY)

    candidates = [0] * BUCKET_CAPACITY
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            lower_part_x = ((x << 16) - 1) & x
            candidates[lower_part_x] = 1

    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure("{} appears in stream".format(res))
    except ValueError:
        raise TestFailure("Unexpected no missing element exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "absent_value_array.py",
            "absent_value_array.tsv",
            find_missing_element_wrapper,
        )
    )
