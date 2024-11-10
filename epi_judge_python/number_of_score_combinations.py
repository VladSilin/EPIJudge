from typing import List

from test_framework import generic_test

# Play:
# safety_pts = 2
# field_goal_pts = 3
# touchdown_pts = 7

# Input: final_score, individual_play_scores
# Ouput: number_of_combinations_leading_to_final_score

# Approach 1: Multiply each index
# 4, [1, 2] -> 1 1 1 1, 1 1 2, 2 2

# cur_num = nums[0]
# for i in range(0, final_score // cur_num):
#    score += cur_num * i + score(nums with no cur_num)

# Base case(s)? nums is [], score == final_score?

# Issues:
# - For loop limit changes with each recursive call
# - Must keep track of variable (state) outside of recursive call
# - LACK OF CONFIDENCE IN APPROACH *

'''
Notes:
    - 2 (3?) ways of keeping state in recursion:
        - nonlocal variable
        - passing an argument to the recursive call
        - as the return value of the function?
    - Remember: Recursion always goes "deep"
        - Indenting is useful in examples
        
    - In first solution: no overlapping subproblems, so cannot do DP/memoization
'''


# 12: [2, 3, 7]
# Allowed: 2 -> (_6*2) -> 1 comb.

# Allowed 2, 3 -> #(_0*2, _4*3)#, (_1*2, XX*3), (_2*2, XX*3), #(_3*2, _2*3)#, (_4*2, XX*3), (_5*2, XX*3), (_6*2,
# XX*3) -> 2 comb.

# 12 % 2 = 0 -> 1
#   12 % 3 = 0 -> 2
#     12 % 7 != 0 -> 2
#     9 % 7 != 0 -> 2
#     6 % 7 != 0 -> 2
#   10 % 3 != 0 -> 2
#     10 % 7 != 0 -> 2
#     7 % 7 == 0 -> 3
#   8 % 3 != 0 -> 3
#     8 % 7 != 0 -> 3
#     5 % 7 != 0 -> 3
#   6 % 3 == 0 -> 4
#     6 % 7 != 0 -> 4

# 4, [1, 2]

def permutations_of_string(s: str):
    def _permutations_of_string(processed: str, rest: str):
        if rest == '':
            print(processed)

            return

        for i in range(0, len(rest)):
            next_processed = processed + rest[i]
            next_rest = rest[0:i] + rest[i + 1:]

            _permutations_of_string(next_processed, next_rest)

    _permutations_of_string('', s)


def num_combinations_for_final_score0(final_score: int,
                                      individual_play_scores: List[int]) -> (int, List[int]):
    count = 0

    # Problem: Successful scores are double-counted
    # Root Cause: Example: For 1 '2': 0 '3's and 1 '7' is tried. Also for 1 '2': 1 '7' is tried.
    def _num_combinations_for_final_score0(cur_score_index: int, remainder: int,
                                           individual_play_scores: List[int]):
        score = individual_play_scores[cur_score_index]

        # Since the loop below will run to and including the possible number
        # of the previous score, at some points it will divide equally.
        # This case will have already been counted and must not be double-counted
        # by the remainder arithmetic below
        if remainder == 0:
            return

        if remainder % score == 0:
            nonlocal count
            count += 1

        # At the last score, no need to look at any others
        if cur_score_index == len(individual_play_scores) - 1:
            return

        # Add 1 to make sure that the for-loop runs at least once
        # E.g. for the case where 'remainder' < 'score', we still want to run
        # combinations with 0 instances of 'score'.
        possible_num = remainder // score + 1

        for i in range(0, possible_num):
            _num_combinations_for_final_score0(cur_score_index + 1, remainder - score * i, individual_play_scores)

    _num_combinations_for_final_score0(0, final_score, individual_play_scores)

    return count


def num_combinations_for_final_score2(final_score: int,
                                      individual_play_scores: List[int]) -> (int, List[int]):
    num_combinations = 0

    def _num_combinations_for_final_score2(final_score: int, individual_play_scores: List[int],
                                           current_combination: List[int], winning_combinations: List[List[int]],
                                           sequence_map: set[str]):
        # 4, [1, 2] -> 1 1 1 1, 1 1 2, 2 1 1, 2 2
        if final_score == 0:
            current_combination_stringified = str(sorted(current_combination))

            if current_combination_stringified not in sequence_map:
                nonlocal num_combinations
                num_combinations += 1

                sequence_map.add(current_combination_stringified)
                winning_combinations.append(current_combination.copy())

            if current_combination:
                current_combination.pop()

            return
        elif final_score < 0:
            if current_combination:
                current_combination.pop()

            return

        for score in individual_play_scores:
            # 1
            current_combination.append(score)
            # 1, [1, 2], [1, 1, 1], []
            _num_combinations_for_final_score2(final_score - score, individual_play_scores, current_combination,
                                               winning_combinations, sequence_map)
        if current_combination:
            current_combination.pop()

    winning_combinations = []
    sequence_map = set()
    _num_combinations_for_final_score2(final_score, individual_play_scores, [], winning_combinations, sequence_map)

    return num_combinations, winning_combinations


# [2, 3, 7]

# ONLY 2's
# 12 (6 2's) -> 2 * 6 -> 1

# 2's AND 3's
# 9 (1 3's) -> 2 * X -> X
# 6 (2 3's) -> 2 * 3 -> 2
# 3 (3 3's) -> 2 * X -> X
# 0 (4 3's) -> X -> X

# 2's AND 3's AND 7's
# 12 (0 7's) -> 3 * 4 -> 3
# 5 (1 7's) -> 2 * 1 + 3 * 1 -> 4
def num_combinations_for_final_score3(final_score: int,
                                      individual_play_scores: List[int]) -> (int, List[int]):
    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            if i < 1:
                num_combinations_for_score[i][j] = 1 if j % individual_play_scores[i] == 0 else 0
                continue

            how_many_of_this_play = 0
            with_multiple_of_this_play = 0

            while j - how_many_of_this_play >= 0:
                with_multiple_of_this_play += num_combinations_for_score[i - 1][
                    j - how_many_of_this_play] if j >= how_many_of_this_play else 0

                how_many_of_this_play += individual_play_scores[i]

            num_combinations_for_score[i][j] = with_multiple_of_this_play

    return num_combinations_for_score[-1][-1]


def num_combinations_for_final_score(final_score: int, individual_play_scores: [int]) -> int:
    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (num_combinations_for_score[i - 1][j] if i > 0 else 0)

            with_this_play = (
                num_combinations_for_score[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0)

            num_combinations_for_score[i][j] = (without_this_play + with_this_play)

    return num_combinations_for_score[-1][-1]


if __name__ == '__main__':
    # print(num_combinations_for_final_score3(12, [2, 3, 7]))
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
