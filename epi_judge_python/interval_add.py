import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple("Interval", ("left", "right"))

# Inputs:
# disjoint_intervals: List[Interval], a list of disjoint intervals, sorted by left endpoint
# new_interval: Interval, a new interval

# Outputs:
# new_intervals: List[Interval], a new list of disjoint intervals, sorted by left endpoint

# Notes / Assumptions:
# - Assume intervals are well-formed (left < right)
# - The new interval either
#   - Splits
#   - Subsumes
#   - Falls within
#   A set of the existing intervals.

# Examples:

# Outline:
# - Go through the array, copying over intervals until one is reached where
# left is between existing_left and existing_right
# - Save the 1st "stopped" interval
# - Keep going through intervals (without copying) until either existing_right
# is greater than right, or the last interval is reached
# - Take left of the stopped existing interval and the max(right, last_interval)


#     [[     ]     [  ]      [   ]]
# 1.   [ ]
# 2.    [ ]
# 3.    [     ]
# 4.    [           ]
# 5.    [                        ]


# NOTE: This one is more efficient (7ms vs 34ms)
def add_interval0(
    disjoint_intervals: List[Interval], new_interval: Interval
) -> List[Interval]:
    if not disjoint_intervals:
        return [new_interval]

    new_intervals = []

    # Append intervals until
    #   - An intersecting one is found OR
    #   - One that is entirely AFTER new_interval
    first_relevant_interval = None
    for existing_interval in disjoint_intervals:
        if (
            existing_interval.right >= new_interval.left
            or existing_interval.left >= new_interval.left
        ):
            first_relevant_interval = existing_interval
            break

        new_intervals.append(existing_interval)

    # Find the interval which
    #   - Either entirely AFTER new_interval OR
    #     - Then, go back one
    #   - Is NOT entirely after, but has a `right` which is after
    #   `new_interval.right` (i.e. this means it intersects) OR
    #   - The last interval is reached
    last_relevant_interval_idx = 0
    for existing_interval in disjoint_intervals:
        if existing_interval.left > new_interval.right:
            last_relevant_interval_idx -= 1
            break
        elif (
            existing_interval.right >= new_interval.right
            or last_relevant_interval_idx == len(disjoint_intervals) - 1
        ):
            break

        last_relevant_interval_idx += 1

    insert_start = (
        new_interval.left
        if not first_relevant_interval
        else min(first_relevant_interval.left, new_interval.left)
    )
    insert_end = (
        new_interval.right
        if last_relevant_interval_idx == -1
        else max(
            disjoint_intervals[last_relevant_interval_idx].right, new_interval.right
        )
    )

    new_intervals.append(Interval(left=insert_start, right=insert_end))

    new_intervals.extend(disjoint_intervals[last_relevant_interval_idx + 1 :])

    return new_intervals


def add_interval(
    disjoint_intervals: List[Interval], new_interval: Interval
) -> List[Interval]:
    i, result = 0, []

    # Process intervals which come before new_interval
    while (
        i < len(disjoint_intervals) and new_interval.left > disjoint_intervals[i].right
    ):
        result.append(disjoint_intervals[i])
        i += 1

    # Process intervals which intersect new_interval
    while (
        i < len(disjoint_intervals) and new_interval.right >= disjoint_intervals[i].left
    ):
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right),
        )
        i += 1

    # Combine all (including the "rest" which come after new_interval
    return result + [new_interval] + disjoint_intervals[i:]


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals, Interval(*new_interval))
    )


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    # in1 = [
    #     Interval(-4, -1),
    #     Interval(0, 2),
    #     Interval(3, 6),
    #     Interval(7, 8),
    #     Interval(11, 12),
    #     Interval(14, 17),
    # ]
    # added = Interval(9, 10)
    # res = add_interval(in1, added)
    # print(res)
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            "interval_add.tsv",
            add_interval_wrapper,
            res_printer=res_printer,
        )
    )
