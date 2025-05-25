import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple("Person", ("age", "name"))


# Input:
# people: List[Person], Person: (age, name), a list of (age, name) tuples

# Output:

# Notes / Assumptions:

# Examples:

# Outline:
# - Brute force: Sort by age, O(n * log(n))


def group_by_age0(people: List[Person]) -> None:
    age_to_tuple = collections.defaultdict(list)

    for p in people:
        age_to_tuple[p.age].append(p)

    i = 0
    for people_by_age in age_to_tuple.values():
        for person in people_by_age:
            people[i] = person
            i += 1


def group_by_age(people: List[Person]) -> None:
    age_to_count = collections.Counter(p.age for p in people)

    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        # TODO: Add to notes (use next() rather than index)
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]

        # Get the age that's at the offset of the current age
        to_age = people[from_idx].age

        # Find the appropriate index to place the offset that's
        # at the offset of the current age
        to_idx = age_to_offset[to_age]

        # Swap the people to ensure they are in the appropriate groups
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure("Empty result")

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure("Entry set changed")

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure("Entries are not grouped by age")
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "group_equal_entries.py", "group_equal_entries.tsv", group_by_age_wrapper
        )
    )
