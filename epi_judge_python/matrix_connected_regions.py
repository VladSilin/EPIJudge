import collections
from typing import List

from test_framework import generic_test


# Input:
# image: List[List[bool]], an n x m bool matrix of booleans (black / white)
# x, y: int, a coordinate; y: outer list index, x: inner list index i.e. image[y][x] is the correct point

# Output:
# (in-place) image, with all entries of same color adjacent to image[y][x] flipped

# Notes / Assumptions:
# - 2D array of colors (black and white, boolean)
# - Adjacency: to (left, right, below, above)
#   - Adjacency is symmetric
#
# - y: outer list index, x: inner list index i.e. image[y][x] is the correct point

# Examples:

# X X X X X X
# X O X X X X
# O O O X X X
# X O 0 X X X
# X O X X X X

# Input:
# [
# [0, 0, 1, 1, 1, 1],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 0, 0, 1, 1],
# [1, 1, 0, 0, 1, 0],
# [0, 1, 0, 1, 1, 1],
# [1, 1, 1, 1, 1, 1]
# ]

# Expected:
# [
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0]
# ]


# O X O
# X O X
# O X X

# Brute Force:
# Optimized:
def flip_color0(x: int, y: int, image: List[List[bool]]) -> None:
    n = len(image)
    m = 0 if not image else len(image[0])
    visited = set()
    # TODO: Use deque
    q = [(x, y)]

    to_paint = set()

    def mark(_x, _y):
        to_paint.add((_x, _y))

    while q:
        cur = q.pop(0)

        cx, cy = cur[0], cur[1]
        color = image[cx][cy]
        mark(*cur)
        visited.add(cur)

        adj = [c for c in [
            (max(0, cx - 1), cy),
            (cx, min(n - 1, cy + 1)),
            (cx, max(0, cy - 1)),
            (min(m - 1, cx + 1), cy),
        ] if c != (cx, cy)]

        for coord in adj:
            if coord not in visited and image[coord[0]][coord[1]] == color:
                # Issue:
                # - Adjacents are added to q from point A (not yet "visited"/"colored")
                # - Same adjacents may be added to q from point B
                # TODO: Add to notes (if "visiting" nodes "after" queueing them, it's possible to have repetitions)
                # TODO: Look up BFS impls. to see if this is a known edge case
                #   - This may be a consideration unique to adjacency matrix representation?
                #   - Note that this representation is NOT an adjacency matrix
                q.append(coord)

    for coord in to_paint:
        image[coord[0]][coord[1]] = int(not image[coord[0]][coord[1]])


def flip_color1(x: int, y: int, image: List[List[bool]]) -> None:
    n = len(image)
    m = 0 if not image else len(image[0])
    # visited = set()
    # TODO: Use deque
    q = [(x, y)]

    # to_paint = set()

    def mark(_x, _y):
        image[_x][_y] = int(not image[_x][_y])
        # to_paint.add((_x, _y))

    color = image[x][y]
    while q:
        cur = q.pop(0)

        cx, cy = cur[0], cur[1]

        # TODO: Add to notes (be careful comparing tuples with '!=')
        adj = [c for c in [
            (max(0, cx - 1), cy),
            (cx, min(n - 1, cy + 1)),
            (cx, max(0, cy - 1)),
            (min(m - 1, cx + 1), cy),
        ] if c is not (cx, cy)]

        for coord in adj:
            if image[coord[0]][coord[1]] == color:
                # TODO: Figure out this key 'mark()' placement
                # NOTE: This is NOT a "visit" operation! A visit operation occurs after popping if you want visits to
                # occur in breadth-first order. The visit operation is in fact the entire loop (i.e. visit == f(all neighbours)
                # in this case
                mark(*coord)
                q.append(coord)

    # for coord in to_paint:
    #     image[coord[0]][coord[1]] = int(not image[coord[0]][coord[1]])

def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

    color = image[x][y]
    q = collections.deque([Coordinate(x, y)])
    image[x][y] = 1 - image[x][y]
    while q:
        x, y = q.popleft()
        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_x, next_y = x + d[0], y + d[1]

            if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])) and image[next_x][next_y] == color:
                image[next_x][next_y] = 1 - image[next_x][next_y]
                q.append(Coordinate(next_x, next_y))

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    #input = [
    #    [0, 0, 1, 1, 1, 1],
    #    [0, 0, 0, 0, 1, 0],
    #    [0, 0, 0, 0, 1, 1],
    #    [1, 1, 0, 0, 1, 0],
    #    [0, 1, 0, 1, 1, 1],
    #    [1, 1, 1, 1, 1, 1]
    #]

#    input = [
#        [0, 1, 0],
#        [1, 1, 1],
#        [0, 1, 0]
#    ]
    #flip_color(0, 4, input)

    #print(input)

    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
