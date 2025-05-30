from typing import List

from test_framework import generic_test

# Input:
# s: str, a string representing an IP address without periods

# Output:
# valid_ips: List[str], a list of all possible valid IPs corresp. to the string

# Notes / Assumptions:

# Example:
# 19216811
# [1.9.2.16811]

# Outline:
def get_valid_ip_address(s: str) -> List[str]:
    def is_valid_part(s):
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

    result, parts = [], [None] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]

        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i + j:i + j + k], s[i + j + k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))

    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
