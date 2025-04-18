from typing import List

from test_framework import generic_test, test_utils

# Input:
# phone_number: str, a number spec. as a string of digits

# Output:
# words: List[str]: All phone keypad strings which could corresp. to that number

# Notes / Assumptions:

# Example:

# Outline:

def phone_mnemonic(phone_number: str) -> List[str]:
    digit_mapping = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

    def _phone_mnemonic(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for c in digit_mapping[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                _phone_mnemonic(digit + 1)

    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    _phone_mnemonic(0)

    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
