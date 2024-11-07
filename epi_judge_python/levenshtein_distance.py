from test_framework import generic_test


# Operations: (i)nsertion, (d)eletion, (s)ubstitution
# Output: Min. num. edits to transform A into B
#
# A: Saturday
# B: Sundays
#
# A: Sundays
# B: Sundays
# d, d, s, i
#
# A: Saturday
# B: Sundays
#
# A: Sat
# B: Sun
#
# A: Sat
# B: Sun
# (S, S) -> Do nothing, move on to (a, u)
# (a, u) -> (s)ubstitute a with u, move on to (t, n)
# (t, n) -> (s)ubstitute t with n, done.
#
# Rules:
#   - If char is the same, do nothing
#   - If char is different, try:
#     - Delete
#     - Substitute (with char at B's position)
#     - (If len(A) < len(B)) Insert char at B's position
def levenshtein_distance0(A: str, B: str) -> int:
    # TODO - you fill in here.
    def new_string_distance_to_original(new_string: str, _B: str, i):
        if new_string[i] == _B[i]:
            return 0
        else:
            count = 1
            string_after_delete = new_string[:i] + new_string[i + 1:]
            string_after_subsitute = new_string[:i] + _B[i] + new_string[i + 1:]

            if len(new_string) < len(_B):
                string_after_insert = new_string[:i + 1] + _B[i + 1] + new_string[i + 1:]
            else:
                count = 0

            return 1

    return 0


def levenshtein_distance1(A: str, B: str) -> int:
    def _levenshtein_distance(_A: str, _B: str, i: int, j: int) -> int:
        # TODO: Add to notes (debugging technique: go through symmertrical statements
        #  (e.g. i in if to j in return, j in if to i in return to make sure you're using the right one)
        if i == 0:
            return j
        elif j == 0:
            return i

        num_operations_to_sub_last_char = 0 if _A[i - 1] == _B[j - 1] else 1

        return min([
            _levenshtein_distance(_A, _B, i - 1, j) + 1,
            _levenshtein_distance(_A, _B, i, j - 1) + 1,
            _levenshtein_distance(_A, _B, i - 1, j - 1) + num_operations_to_sub_last_char
        ])

    return _levenshtein_distance(A, B, len(A), len(B))


# TODO: Add to notes (good recursion step-through approach)
# L(A, B) -> 1
#   num_ops = 1
#   min = 1
#   L('', B) + 1 -> 2
#     return 1
#   L(A, '') + 1 -> 2
#     return 1
#   L('', '') + num_ops -> 1
#     return 0
#
# The three terms correspond to transforming A to B by the following three ways:
# - Transforming [Sat] to [Sun] by transforming [Sa]t to [Su]n and then
# substituting A's last character with B's last character.
# [Sa]t
#     v
# [Su]n
#
# - Transforming [Sat] to [Sun] by transforming [Sat] to [Su]n and then
# adding B's last character at the end.
# [Sat]
#     +
# [Su]n
#
# - Transforming [Sat] to [Sun] by transforming [Sa]t to [Sun] and then
# deleting A's last character.
# [Sa]t
#     x
# [Sun]
#
# TODO: Add to notes (Be mindful of the examples you choose
#  E.g. The deletion operation appears logical in the example of [Sun]f -> [Sun]
#  But is difficult to understand when considering [Sa]t to [Sun]
#  (Because it looks so obviously wrong).
#  Still, this operation is necessary to be sure the algorithm considers all options)
# [Sun]f
# [Sun]
def levenshtein_distance2(A: str, B: str) -> int:
    # If reached a point where A is empty, can reach B by len(B) insertions
    if A == '':
        return len(B)
    # If reached a point where B is empty, can reach A by len(A) deletions
    elif B == '':
        return len(A)

    num_operations_to_sub_last_char = 0 if A[-1] == B[-1] else 1

    # NOTE: +1 => Edit step
    return min(
        # Assume a deletion, find distance from A[0:len(A) - 1] to B
        [levenshtein_distance2(A[:-1], B) + 1,
         # Assume an insertion, find distance from A to B[0:len(B) - 1]
         levenshtein_distance2(A, B[:-1]) + 1,
         # Assume a substitution or noop
         levenshtein_distance2(A[:-1], B[:-1]) + num_operations_to_sub_last_char]
    )


#   - S u n
# - 0 1 2 3
# S 1 0 x
# a 2
# t 3
def levenshtein_distance(A: str, B: str) -> int:
    m = len(A)
    n = len(B)

    # TODO: Add to notes (with arrays of arrays, the indexing starts at the 'top left corner', with
    #   (y, x) -> [y][x] coordinates
    # TODO: Add to notes (the start of range() is inclusive but the end is exclusive, i.e. [start, end))
    # TODO: Add to notes (Generate 2D matrix)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # TODO: Add to notes (tricky index stuff: the loop populates indices from 0 to len(A) and len(B) inclusive.
    #   The 1st character of B is represented by dp[i][1] and of B at dp[1][j]
    #   The last character of A is represented by dp[i][len(A)] and of B at dp[len(B)][j]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            num_operations_to_sub_last_char = 0 if A[i - 1] == B[j - 1] else 1
            dp[i][j] = min([
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + num_operations_to_sub_last_char,
            ])

    return dp[m][n]


if __name__ == '__main__':
    #result = levenshtein_distance('Saturday', 'Sunday')
    #print(result)
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
