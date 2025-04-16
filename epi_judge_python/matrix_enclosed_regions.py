import collections
from typing import List

from test_framework import generic_test

# Inputs:
# board: List[List[str]], a 2D array of 'W', 'B'

# Outputs:
# board, with all 'W' squares which are enclosed (cannot reach boundary) painted 'B'

# Notes / Assumptions:

# Example:
# X X X
# X O X
# X X X

# X X X
# O X X
# X X X

# X X X
# O O X
# X X X

# X X X X X
# X O O X X
# X X X X X
# X O O X X
# X X O X X

# Brute Force Outline:
# - Go through each elem. until 'W' found
# - Once unvisited 'W' found, start BFS
#
# while not reached a boundary:
#   - Record each visited node
#   - Record the nodes to paint
#
# boundary reached:
#   - Clear the nodes to paint
#
# once done:
#   - Paint all remaining recorded nodes

# Optimal Outline:
def fill_surrounded_regions0(board: List[List[str]]) -> None:
    Coord = collections.namedtuple('Coord', ('x', 'y'))
    visited = set()
    to_paint = set()

    is_boundary = lambda _x, _y: ((_x <= 0 or _x >= len(board)) or
                                  (_y <= 0 or _y >= len(board[_x])))
    for x in range(len(board)):
        for y in range(len(board[x])):
            elem = board[x][y]
            if is_boundary(x, y) or elem == 'B' or (x, y) in visited:
                continue

            q = collections.deque([Coord(x, y)])
            while q:
                cur = q.popleft()

                visited.add(cur)
                to_paint.add(cur)

                for d in (1, 0), (-1, 0), (0, 1), (0, -1):
                    next_x, next_y = x + d[0], y + d[1]

                    if ((next_x < 0 or next_x >= len(board)) or
                        (next_y < 0 or next_y >= len(board[next_x])) or
                        board[next_x][next_y] == 'B' or
                        Coord(next_x, next_y) in visited):
                        continue
                    elif is_boundary(next_x, next_y):
                        for c in to_paint:
                            board[c.x][c.y] = 'B'
                        to_paint = set()
                    else:
                        q.append(Coord(next_x, next_y))

    print(to_paint)

def fill_surrounded_regions(board: List[List[str]]) -> None:
    n, m = len(board), len(board[0])
    # TODO: Add to notes (can start BFS from multiple points by adding many to queue)
    q = collections.deque([
        (i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))
    ] + [(i, j) for k in range(m) for i, j in ((0, k), (n - 1, k))])

    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
            board[x][y] = 'T'
            q.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]

def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    #input1 = [
    #   ['B', 'B', 'B', 'W', 'W'],
    #   ['B', 'W', 'W', 'B', 'B'],
    #   ['B', 'B', 'B', 'B', 'B'],
    #   ['B', 'B', 'W', 'W', 'B'],
    #   ['W', 'W', 'B', 'B', 'B']
    #]

    #fill_surrounded_regions(input1)
    #print(input1)
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
