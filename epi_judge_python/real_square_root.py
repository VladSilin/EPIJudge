import math

from test_framework import generic_test

# Inputs:
# x: float, a floating point number

# Outputs:
# square_root: float, the square root of the number

# Notes / Assumptions:

# Example:
# x = 5
# 1 * 1 = 1
# 2 * 2 = 4
# 2.125 * 2.125 = 4.52
# etc.
# 2.25 * 2.25 =  5.06
# 2.5 * 2.5 = 6.25
# 3 * 3 = 9

# Outline:
# - Go through all numbers 1 to x and square them (at a certain resolution)
# - Once reached close enough to x, return

# Optimized:
# - Find first square larger than x
# - Take mid = smaller + (larger - smaller) / 2
#   - Find square of this
#   - If bigger, search left
#   - If smaller, search right


def square_root(x: float) -> float:
    l, h = (x, 1.0) if x < 1.0 else (1.0, x)
    while not math.isclose(l, h):
        m = l + (h - l) / 2
        m_squared = m**2

        if m_squared > x:
            h = m
        else:
            l = m

    return l


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "real_square_root.py", "real_square_root.tsv", square_root
        )
    )
