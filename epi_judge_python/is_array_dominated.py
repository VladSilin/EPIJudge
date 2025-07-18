import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Input:

# Output:

# Notes / Assumptions:

# Examples:

# Outline:


class Team:
    Player = collections.namedtuple("Player", ("height"))

    def __init__(self, height: List[int]) -> None:
        self._players = [Team.Player(h) for h in height]

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0: "Team", team1: "Team") -> bool:
        return all(
            a < b for a, b in zip(sorted(team0._players), sorted(team1._players))
        )


@enable_executor_hook
def valid_placement_exists_wrapper(executor, team0, team1, expected_01, expected_10):
    t0, t1 = Team(team0), Team(team1)

    result_01 = executor.run(functools.partial(Team.valid_placement_exists, t0, t1))
    result_10 = executor.run(functools.partial(Team.valid_placement_exists, t1, t0))
    if result_01 != expected_01 or result_10 != expected_10:
        raise TestFailure("")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_array_dominated.py",
            "is_array_dominated.tsv",
            valid_placement_exists_wrapper,
        )
    )
