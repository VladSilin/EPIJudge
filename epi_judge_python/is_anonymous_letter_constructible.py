from test_framework import generic_test
from collections import defaultdict


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    magazine_char_counts: dict[str, int] = defaultdict(lambda: 0)

    for magazine_char in magazine_text:
        magazine_char_counts[magazine_char] += 1

    for letter_char in letter_text:
        # Look through the letters; If for any of the letters the count is not initialized (doesn't exist)
        # or the count has reached 0 there are not enough characters in the magazine, thus return false.
        if magazine_char_counts[letter_char] == 0:
            return False
        else:
            # Otherwise, one or more of this character exists in the magazine, so decrement the count to "use it"
            magazine_char_counts[letter_char] = magazine_char_counts[letter_char] - 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
