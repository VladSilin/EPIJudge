import functools
from typing import List
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

# TODO: Add to notes (random permutations not straightforward reasoning from book, also Coupon Collector's Problem)
# The total number of ways in which we can choose
# the elements to swap is 3 ** 3 = 27 and all are equally likely. Since 27 is not divisibleby 6, some
# permutations correspond to more ways than others, so not all permutations are equally likely.
#
# TODO: Add to notes (permutations vs combinations, repeated elements vs not)
# [1, 2, 3]

# [1, 2, 3] swap 0, 0
  # [1, 3, 2]
# [2, 1, 3] swap 0, 1
  # [2, 3, 1]
# [3, 2, 1] swap 0, 2
  # [3, 1, 2]

# Input:
# n: int, number of elements for random selection; k: int, size of random subset

# Output:
# a random subset of the numbers [0, 1, ..., n - 1] (all subsets should be equally likely)

# Notes / Assumptions:

# Example:

# TODO: Add to notes (use a map to emulate a mapping of a subset of array elements)
def random_subset(n: int, k: int) -> List[int]:
    changed_elements = {}

    for slot in range(k):
        random_index = random.randrange(slot, n)
        random_index_value = changed_elements.get(random_index, random_index)

        slot_value = changed_elements.get(slot, slot)
        changed_elements[random_index] = slot_value
        changed_elements[slot] = random_index_value

    return [changed_elements[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    n_input = 100
    k_input = 4

    result = random_subset(n_input, k_input)

    print(result)

    #exit(
    #    generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
    #                                   random_subset_wrapper))
