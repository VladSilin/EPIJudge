import functools
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_sampling2(k: int, A: List[int]) -> None:
    init_num_elements = len(A)
    for i in range(init_num_elements - k):
        s = random.randint(0, len(A) - 1)
        print('Len:', len(A))
        print('s:', s)
        A.remove(A[s])
        print(A)

    return


def random_sampling(k: int, A: List[int]) -> None:
    for i in range(k):
        random_index = random.randint(i, len(A) - 1)

        A[i], A[random_index] = A[random_index], A[i]

    return


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    sample_size = 3
    samples = [1, 2, 3, 4, 5, 6, 7]
    random_sampling(sample_size, samples)
    print(samples[:sample_size])

    # exit(
    #     generic_test.generic_test_main('offline_sampling.py',
    #                                    'offline_sampling.tsv',
    #                                    random_sampling_wrapper))
