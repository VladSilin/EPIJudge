import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:
# num_bits: int, number of bits for numbers

# Output:
# gray_integers: List[int], permutation of integers following the Gray code

# Notes / Assumptions:

# Examples:
# n = 2  =>  0, 1, 2, 3
# 01, 00, 10, 11
# 10, 00, 01, 11

# n = 3  =>  0, 1, 2, 3, 4, 5, 6, 7

# Outline:


def differ_by_1_bit(x, y):
    bit_difference = x ^ y
    # TODO: Add to notes (common trick for checking if a number is a power of two (has one bit set))
    return bit_difference and not (bit_difference & (bit_difference - 1))


def gray_code0(num_bits: int) -> List[int]:
    result = [0]

    def directed_gray_code(history):
        def differs_by_one_bit(x, y):
            bit_difference = x ^ y
            # TODO: Add to notes (common trick for checking if a number is a power of two (has one bit set))
            return bit_difference and not (bit_difference & (bit_difference - 1))

        if len(result) == 1 << num_bits:
            # Check if the first and last codes differ by one bit
            return differs_by_one_bit(result[0], result[-1])

        for i in range(num_bits):
            previous_code = result[-1]
            # TODO: Add to notes (XOR with bit in a position to flip that bit)
            candidate_next_code = previous_code ^ (1 << i)
            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)
                if directed_gray_code(history):
                    return True
                history.remove(candidate_next_code)
                del result[-1]

        return False

    directed_gray_code(set([0]))

    return result


def gray_code(num_bits: int) -> List[int]:
    if num_bits == 0:
        return [0]

    # These implicitly begin with 0 at bit_index (num_bits - 1)
    gray_code_num_bits_minus_1 = gray_code(num_bits - 1)

    # Now, add a 1 at bit_index (num_bits - 1) to all entries in
    # gray_code_num_bits_minus_1
    leading_bit_one = 1 << (num_bits - 1)

    # Process in reverse order to achieve reflection of
    # gray_code_numb_bits_minus_1
    return gray_code_num_bits_minus_1 + [
        leading_bit_one | i for i in reversed(gray_code_num_bits_minus_1)
    ]


def gray_code_pythonic(num_bits: int) -> List[int]:
    result = [0]
    for i in range(num_bits):
        result += [x + 2**i for x in reversed(result)]

    return result


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = 1 << num_bits
    if len(result) != expected_size:
        raise TestFailure(
            "Length mismatch: expected "
            + str(expected_size)
            + ", got "
            + str(len(result))
        )
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure("Two adjacent entries are equal")
            else:
                raise TestFailure("Two adjacent entries differ by more than 1 bit")

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure(
            "Not all entries are distinct: found "
            + str(len(result) - len(uniq))
            + " duplicates"
        )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "gray_code.py", "gray_code.tsv", gray_code_wrapper
        )
    )
