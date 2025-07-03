from test_framework import generic_test

# Inputs:
# n: int, number of rows (num lists)
# m: int, number of columns (size of each list)
# - n and m are the dimensions of a 2D array

# Outputs:
# num_ways_to_traverse: int, the number of ways to get from 'top left' to 'bottom right' corner

# Notes / Assumptions:
# - n and m can be different (not square)
# - Bounds on n, m?
# - top_left: 2d_array[0][0], bottom_right: 2d_array[len - 1][len - 1]
# - All moves go right or down

# Examples:
# 2 x 2
#
# X X X
# X X X
# X X X
#
# i, j, is_on_edge
# i = 0, j = 0, is_on_edge = False,
#   actions: i += 1 or j += 1
#       i = 1, j = 0, is_on_edge = False,
#           actions: i += 1 or j += 1


# Outline:
def number_of_ways0(n: int, m: int) -> int:
    dp = [[0] * m for _ in range(n)]

    def num_ways_from_position_to_corner(i: int, j: int):
        is_done = i == n - 1 and j == m - 1
        if is_done:
            return 1

        given_move_i, given_move_j = 0, 0
        if dp[i][j] == 0:
            if i + 1 < n:
                given_move_i = num_ways_from_position_to_corner(i + 1, j)
            if j + 1 < m:
                given_move_j = num_ways_from_position_to_corner(i, j + 1)

            dp[i][j] = given_move_i + given_move_j

        return dp[i][j]

    return num_ways_from_position_to_corner(0, 0)


def number_of_ways(n: int, m: int) -> int:
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = 1
    for i in range(0, n):
        for j in range(0, m):
            num_ways_i = 0 if i - 1 < 0 else dp[i - 1][j]
            num_ways_j = 0 if j - 1 < 0 else dp[i][j - 1]

            dp[i][j] = max(1, num_ways_i + num_ways_j)

    return dp[-1][-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_traversals_matrix.py",
            "number_of_traversals_matrix.tsv",
            number_of_ways,
        )
    )
