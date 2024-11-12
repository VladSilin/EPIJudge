from test_framework import generic_test
from test_framework.test_failure import TestFailure

DIGITS_START = ord('0')


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    sign = '' if x >= 0 else '-'
    output = ''

    x = abs(x)
    while x:
        digit = x % 10
        x = (x - digit) / 10

        output += chr(DIGITS_START + int(digit))

    return sign + output[::-1]


def string_to_int(s: str) -> int:
    sign = s[0]

    int_number = 0
    for i in range(1 if sign == '-' or sign == '+' else 0, len(s)):
        cur_char = s[i]

        digit_val = ord(cur_char) - DIGITS_START
        decimal_val = digit_val * (10 ** (len(s) - 1 - i))

        int_number += decimal_val

    return -int_number if sign == '-' else int_number


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
