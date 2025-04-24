from future.utils import is_new_style

from test_framework import generic_test

# Input:
# x: int, an integer

# Output:
# reversed_digits: int, the integer with reversed digits

# Notes / Assumptions:

# Example:

# Outline:
# - Do x mod 10 ** n
# - Increase n until the number is 0
# 271 / 10 = 27 rem 1
# 27 / 10 = 2 rem 7
# 2 / 10 = 0 rem 2
def reverse0(x: int) -> int:
    is_negative = x < 0
    n = abs(x)

    digits = []
    while n > 0:
        remainder = n % 10
        n = n // 10

        digits.append(remainder)

    result = 0
    for i in range(len(digits)):
        result += digits[i] * 10 ** (len(digits) - 1 - i)

    return -result if is_negative else result


def reverse(x: int) -> int:
    is_negative = x < 0
    n = abs(x)

    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10

    return -result if is_negative else result


if __name__ == '__main__':
    #r = reverse(-1)
    #print(r)
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
