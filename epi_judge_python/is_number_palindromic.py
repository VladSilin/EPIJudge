from test_framework import generic_test
import math

# Input:
# x: int, a decimal number (can be -'ve)

# Output:
# is_palindromic: bool, is the number palindromic

# Notes / Assumptions:

# Example:

# Outline:
def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0

    # TODO: Add to notes (use math.floor(math.log10(x)) + 1 to get the number of digits in x)
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for _ in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False

        # Remove the MSD of x
        x %= msd_mask
        # Remove the LSD of x
        x //= 10

        msd_mask //= 100

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_number_palindromic.py",
            "is_number_palindromic.tsv",
            is_palindrome_number,
        )
    )
