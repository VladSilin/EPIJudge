import collections

from test_framework import generic_test

# Input:
# s: str, a string which may or may not be permuted to a palindrome

# Output:
# can_be_palindrome: bool, is there a permutation p of s such that p is a palindrome?

# Notes / Assumptions:
# - For even len(s), s must have 2 of each character to be permutable to a palindrome
# - For odd len(s), all chars in s must have a duplicate except for one

# Examples:
# edified
# deified

# Brute Force Outline:
# - Generate all permutations of s
# - For each permutation, check if it is a palindrome
# - Return if found

# Optimized:
# - For each char in s:
#   - Check if in hashmap, check if in map, otherwise add
# - If len(s) even:
#   - All chars must have an even count
# - If len(s) odd:
#   - All chars but one must have an even count


def can_form_palindrome0(s: str) -> bool:
    counts = collections.Counter()
    for c in s:
        counts[c] += 1

    num_odd = 0
    for v in counts.values():
        is_even = v % 2 == 0

        if not is_even:
            num_odd += 1

    return num_odd == 1 if len(s) % 2 > 0 else num_odd == 0


def can_form_palindrome(s: str) -> bool:
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
