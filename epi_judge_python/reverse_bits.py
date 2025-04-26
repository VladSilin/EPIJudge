from epi_judge_python_solutions.reverse_bits import PRECOMPUTED_REVERSE
from test_framework import generic_test

# Input:
# x: int, 64 bit unsigned int.

# Output:
# reversed_bits: int, 64 bit unsigned int. w/ bits reversed

# Notes / Assumptions:

# Example:

# Outline:
# - A bit mask starting with 0...001
# - Loop through, shifting left (x << i)
# - Do a bitwise and to get just the digit at i
def reverse_bits(x: int) -> int:
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF

    # TODO: Add to notes (bit sequence precomputed lookup approach)
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE |
            PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
