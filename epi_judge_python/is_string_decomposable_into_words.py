import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:
# dictionary: Set[str], a set of possible words to be contained in a name
# name: str, the name of a website domain

# Output:
# words: List[str], a list of dictionary words contained in the `name`

# Notes / Assumptions:
# - A dictionary word can be contained in the `name` more than once
#   - i.e. words are NOT "used up" when seen

# Examples:
# name = "amanaplanacanal"
# words = "a", "man", "a", "plan", "a", "canal"

# Outline:

# Given the 1st character, is it a word contained in the dict?;
# actions: if contained, add word and look at 2nd char. If not contained, process name[1st to 2nd] char

# Generalized:

# Given the i'th character, is it a word contained in the dict?;
# actions: if contained, add word and look at char i + 1, offset 0. If not contained, process name[i:i + offset] char


# Problems with this solution:
# - Does not consider all valid lengths of words given a starting char
#   - This leads to a "greedy" algorithm which does not attempt all permutations
def decompose_into_dictionary_words0(domain: str, dictionary: Set[str]) -> List[str]:
    def get_found_words_given_char_and_word_length(cur_char_idx, word_length):
        if cur_char_idx + word_length >= len(domain):
            return []

        word = domain[cur_char_idx : cur_char_idx + word_length]

        if word in dictionary:
            return [word] + get_found_words_given_char_and_word_length(
                cur_char_idx + 1, 1
            )
        else:
            return get_found_words_given_char_and_word_length(
                cur_char_idx, word_length + 1
            )

    return get_found_words_given_char_and_word_length(0, 1)


def decompose_into_dictionary_words1(domain: str, dictionary: Set[str]) -> List[str]:
    dp = {}

    def get_found_words_given_char_and_word_length(cur_char_idx):
        if cur_char_idx == len(domain):
            return []
        if cur_char_idx in dp:
            return dp[cur_char_idx]

        for word_length in range(1, (len(domain) - cur_char_idx) + 1):
            word = domain[cur_char_idx : cur_char_idx + word_length]

            if word in dictionary:
                # Look at the rest of the domain starting at cur_char_idx + word_length
                rest = get_found_words_given_char_and_word_length(
                    cur_char_idx + word_length
                )
                if rest is not None:
                    dp[cur_char_idx] = [word] + rest
                    return dp[cur_char_idx]

        dp[cur_char_idx] = None
        return None

    result = get_found_words_given_char_and_word_length(0)
    return result if result is not None else []


def decompose_into_dictionary_words(domain: str, dictionary: Set[str]) -> List[str]:
    last_length = [-1] * len(domain)

    for i in range(len(domain)):
        if domain[: i + 1] in dictionary:
            last_length[i] = i + 1

        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j + 1 : i + 1] in dictionary:
                    last_length[i] = i - j
                    break

    decompositions = []
    if last_length[-1] != -1:
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append(domain[idx + 1 - last_length[idx] : idx + 1])
            idx -= last_length[idx]

        decompositions = decompositions[::-1]

    return decompositions


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary, decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary)
    )

    if not decomposable:
        if result:
            raise TestFailure("domain is not decomposable")
        return

    if any(s not in dictionary for s in result):
        raise TestFailure("Result uses words not in dictionary")

    if "".join(result) != domain:
        raise TestFailure("Result is not composed into domain")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            "is_string_decomposable_into_words.tsv",
            decompose_into_dictionary_words_wrapper,
        )
    )
