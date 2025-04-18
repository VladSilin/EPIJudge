import functools

from epi_judge_python.reverse_digits import reverse
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Input:
# s: List[str], a list of characters representing a string

# Output:
# result: List[str], same list with words reversed

# Notes / Assumptions:

# Example:
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
# ['y', 'l', 't', 's', 'o', 'c', ' ', 's', 'i', ' ', 'm', 'a', 'r'].
#
# ['c', 'o', 's', 't', 'l', 'y', ' ', 'i', 's', ' ', 'r', 'a', 'm'].

# Outline:


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    s.reverse()

    def reverse_word(words, start, end):
        while start < end:
            words[start], words[end] = words[end], words[start]
            start, end = start + 1, end - 1


    word_first_char_idx = 0
    i = 0
    while i < len(s):
        if s[i].isspace():
            reverse_word(s, word_first_char_idx, i - 1)

            while i < len(s) and s[i].isspace():
                i += 1

            word_first_char_idx = i

        i += 1

    reverse_word(s, word_first_char_idx, len(s) - 1)

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))
    reverse(s)

    return ''.join(s_copy)


if __name__ == '__main__':
    #test = ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y']

    #reverse_words(test)
    #print(test)

    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                   reverse_words_wrapper))
