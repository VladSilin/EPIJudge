import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple("Subarray", ("start", "end"))


# Inputs:
# paragraph: List[str], a list of words comprising a paragraph
# keywords: Set[str], a set of keywords

# Outputs:
# start_end: Subarray, the start and end index of `paragraph` for the shortest slice containing all keywords

# Notes / Assumptions:

# Examples:
# a a a a b c d e f f f f f
# ^                       ^

# Brute Force Outline:
# - For each keyword, find its first position in the set
# - Take the min and max positions, which are the start_end Subarray

# Optimized:
# - Go through the paragraph and build an index of word_to_first_index


def find_smallest_subarray_covering_set0(
    paragraph: List[str], keywords: Set[str]
) -> Subarray:
    # TODO - you fill in here.

    WordIndex = collections.namedtuple("WordIndex", ("word", "index"))
    relevant_words = []
    for i, word in enumerate(paragraph):
        if word in keywords:
            relevant_words.append(WordIndex(word, i))

    if not relevant_words:
        raise ValueError("no keywords found")

    already_seen = set()
    left, right = 0, len(relevant_words) - 1

    start, end = relevant_words[left].index, relevant_words[right].index
    while left < right:
        if relevant_words[left].word in already_seen:
            start = relevant_words[left].index
        already_seen.add(relevant_words[left].word)

        if relevant_words[right].word in already_seen:
            end = relevant_words[right].index
        already_seen.add(relevant_words[right].word)

        left += 1
        right -= 1

    return Subarray(start, end)


# Outline:
#
# - For any given left bound, advance the right bound until all keywords are
# covered
# - Once reached a right bound where all keywords are covered, WHILE all
# keywords are covered, keep pushing the left bound (while recording shorter
# "all covered" intervals)
# - Once reached a left bound where a keyword is uncovered, go back up to
# advancing the right bound
#   - NOTE that once a keyword is uncovered by advancing the left bound, it may
#     be impossible to find a covering right bound even at the end of the array.
#     However, the smallest covering subarray will have been saved
def find_smallest_subarray_covering_set(
    paragraph: List[str], keywords: Set[str]
) -> Subarray:
    # Each of keywords_to_cover starts at 1 since `keywords` is a set
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0

    # This outer loop ensures that `right` advances as much as needed to cover
    # all keywords first before the inner `while remaining_to_cover == 0` is entered
    #
    # Then, the inner loop advances `left` by its own logic, at which point the
    # outer loop takes care of `right` again`
    for right, p in enumerate(paragraph):
        if p in keywords_to_cover:
            # If we're in here, then we're looking at a `p` in keywords
            keywords_to_cover[p] -= 1

            # This `if` structure means:
            #   "Only subtract remaining_to_cover if the keyword is seen for
            #   the first time"
            # NOTE: keywords_to_cover can become >= 0 in the `left` loop below
            is_keyword_unseen = keywords_to_cover[p] >= 0
            if is_keyword_unseen:
                remaining_to_cover -= 1
            else:
                pass

        # This loop "tries" to make `remaining_to_cover` become more than 0
        #   How? Understand the inner `if` condition.
        while remaining_to_cover == 0:
            is_smaller_subarray = (result == Subarray(start=-1, end=-1)) or (
                right - left < result.end - result.start
            )

            # Note that result always keeps track of the last smallest valid
            # interval (even if the current left and right are messed up)
            if is_smaller_subarray:
                result = Subarray(start=left, end=right)

            pl = paragraph[left]
            # This is saying: "If the thing at the left pointer is a keyword,
            # it won't be covered anymore once we do `left += 1`"
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1

            left += 1

    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph, keywords)
    )

    if (
        start < 0
        or start >= len(paragraph)
        or end < 0
        or end >= len(paragraph)
        or start > end
    ):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper,
        )
    )
