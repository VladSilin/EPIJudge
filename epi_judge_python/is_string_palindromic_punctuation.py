import string

from test_framework import generic_test

# Input:
# s: str, a string (with non-alphanumeric chars)

# Output:
# is_palindrome: bool, does the string read the same front-to-back as back-to-front?

# Notes / Assumptions:
# - Ignore case

# Example:
# "Able was I, ere I saw Elba!"
# "ablewasiereisawelba"

# Outline:
# - 2 pointers
#     i = 0, j = len(s) - 1
# - If char at both are alphanumeric, compare
# - If different, break, return False
# - If same go on
def is_palindrome(s: str) -> bool:
    i, j, = 0, len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() == s[j].lower():
            i, j = i + 1, j - 1
        else:
            return False

    return True


if __name__ == '__main__':
    #test = '7}y'

    #print(is_palindrome(test))

    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
