import string

from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    is_negative = num_as_string[0] == '-'
    if is_negative:
        num_as_string = num_as_string[1:]

    def get_hex_num(base_str: str):
        return string.hexdigits.index(base_str.lower())

    def get_hex_digit(digit: int):
        # TODO: Add to notes (hexdigits)
        return string.hexdigits[digit].upper()

    def convert_to_base10(num_str: str, base: int):
        base10_num: int = 0
        for i, digit in enumerate(num_str):
            base10_num += get_hex_num(digit) * base ** (len(num_str) - 1 - i)

        return str(base10_num)

    def convert_base10_to_base_n(num: str, base: int):
        highest_power = 0
        power_result = base ** highest_power

        while power_result <= int(num):
            highest_power += 1
            power_result = base ** highest_power

        base_n_num_str = ''
        remainder = int(num)

        # TODO: Add to notes (iterating backwards)
        for p in range(highest_power - 1, -1, -1):
            digit = get_hex_digit(remainder // base ** p)
            base_n_num_str += str(digit)
            remainder = remainder % base ** p

        return base_n_num_str or '0'

    result = convert_base10_to_base_n(convert_to_base10(num_as_string, b1), b2)

    return '-' + result if is_negative else result


if __name__ == '__main__':
    #print(convert_base('0', 6, 6))
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
