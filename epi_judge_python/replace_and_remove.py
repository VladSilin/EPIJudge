import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove1(size: int, s: List[str]) -> int:
    # ['b'] -> ['']
    # ['b', 'c'] -> ['c', '']
    # ['b', 'c', ''] -> ['c', '', '']
    def collapse_back(l: List[str], cur_index):
        j = cur_index + 1
        while j < len(l) and l[j]:
            l[j - 1] = l[j]
            j += 1

        l[j - 1] = ''

    def slide_forward(l: List[str], cur_index, char: str):
        for j in range(cur_index, len(l)):
            temp_char = l[j]
            l[j] = char
            char = temp_char

    # Replace 'a' by 2 'd's
    # Remove 'b'
    # [a,c,d,b,b,c,a]

    final_size = size
    i = 0
    while i < len(s) and s[i]:
        if s[i] == 'b':
            collapse_back(s, i)
        else:
            i += 1

    i = 0
    while i < len(s) and s[i]:
        if s[i] == 'a':
            saved_char = s[i + 1]
            s[i], s[i + 1] = 'd', 'd'
            slide_forward(s, i + 2, saved_char)
            i += 2
            final_size += 1
        else:
            i += 1

    return final_size


def replace_and_remove(size: int, s: List[str]) -> int:
    write_index, count_a = 0, 0

    # TODO: Add to notes (multiple pointers - seek head vs write head)
    # By the end of the array, write head will be size - num_b behind the seek head
    for seek_index in range(size):
        if s[seek_index] != 'b':
            s[write_index] = s[seek_index]
            write_index += 1

        # Also count a's when you see them
        if s[seek_index] == 'a':
            count_a += 1

        # TODO: Add to notes (when implicitly handling a conditional branch whose intent is no effect, put it in
        #  explicitly for debugging)
        # elif s[i] == 'b':
        #     s[write_index] = ''
        #     write_index += 1

    # The -1 is to account for the extra write_index increment after seeing a valid character
    write_index -= 1
    last_valid_char_index = write_index
    cur_index = last_valid_char_index

    # Position the write_index to fit the amount of a's that will be written
    write_index += count_a
    final_size = write_index + 1

    while cur_index >= 0:
        if s[cur_index] == 'a':
            # Can also be s[write_index - 1], s[write_index] = 'd', 'd'
            s[write_index - 1:write_index + 1] = 'dd'
            write_index -= 2
        else:
            s[write_index] = s[cur_index]
            write_index -= 1
            pass

        cur_index -= 1

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    # input = ['a', 'c', 'd', 'b', 'b', 'c', 'a', '', '']
    # input = ['a', 'b', 'a', 'c', '']
    # input = ['a', 'c', 'a', '', '']
    chars = ['b', 'b', 'b', 'b', 'd', 'a']

    # TODO: Add to notes (multi-pointer debugging strategy)
    # ['d', 'a', 'b', 'b', 'd', 'a']
    #                            i
    #             w

    # result = replace_and_remove(6, chars)
    # print(input[:result])

    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
