import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple("Item", ("weight", "value"))


# Input:
# items: List[Item], a list of tuples of ('weight', 'value')
# capacity: int, the weight constraint of the backpack

# Output:
# total_value: int, the total value of the selected items which satisfy the weight constraint

# Notes / Assumptions:
# - The weight need not be minimized, only be less than the `capacity` constraint
# - A greedy approach (always taking the item with the next most optimal cost function) is not viable

# Example:

# Assume sorted.
# items = [($50, 3), ($20, 1), ($10, 4)]
# capacity = 4

# Take 1st item, capacity = 4 - 3 = 1, value = $50
#   Actions: Take 2nd item, capacity = 1 - 1 = 0, value = $70; Leave 2nd item, capacity = 1, value = $50
# Leave 1st item, capacity = 4, value = $0
#   Actions: Take 2nd item, capacity = 4 - 1 = 3, value = $20; Leave 2nd item, capacity = 4, value = $0

# Outline:
# Take items[i], capacity -= items[i].weight, value += items[i].value


def optimum_subject_to_capacity0(items: List[Item], capacity: int) -> int:
    def value_givenCapacity_afterLookingAt(i, c):
        if i == len(items):
            return 0

        taken = (
            0
            if c - items[i].weight < 0
            else (
                value_givenCapacity_afterLookingAt(i + 1, c - items[i].weight)
                + items[i].value
            )
        )
        left = value_givenCapacity_afterLookingAt(i + 1, c)

        return max(taken, left)

    result = value_givenCapacity_afterLookingAt(0, capacity)

    return result


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    V = [[-1] * (capacity + 1) for _ in items]

    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0

        if V[k][available_capacity] == -1:
            without_cur_item = optimum_subject_to_item_and_capacity(
                k - 1, available_capacity
            )
            with_cur_item = (
                0
                if available_capacity < items[k].weight
                else items[k].value
                + optimum_subject_to_item_and_capacity(
                    k - 1, available_capacity - items[k].weight
                )
            )
            V[k][available_capacity] = max(without_cur_item, with_cur_item)

        return V[k][available_capacity]

    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == "__main__":
    # r = optimum_subject_to_capacity(
    #     [Item(weight=15, value=17), Item(weight=2, value=7)], 15
    # )
    exit(
        generic_test.generic_test_main(
            "knapsack.py", "knapsack.tsv", optimum_subject_to_capacity_wrapper
        )
    )
