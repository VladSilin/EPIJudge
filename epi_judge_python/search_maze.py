import collections
import copy
import functools
# from collections import OrderedDict
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
ChildParent = collections.namedtuple('ChildParent', ('child', 'parent'))


# e = Coordinate(x=3, y=4)
# print(s)
# print(e, '\n')
# print('      ', end='')
# for p in range(len(maze[s.x])):
#     print(p, end='   ')
# print()
#
# for i in range(len(maze)):
#     print(i, end=(len(str(len(maze))) - len(str(i)) + 1) * ' ' + '|  ')
#
#     for j in range(len(maze[s.x])):
#         print(maze[i][j], end='   ')
#
#     print()

def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    # BFS queue
    queue = []

    x_size = len(maze) - 1
    y_size = len(maze[s.x]) - 1

    visited = collections.OrderedDict()

    def _visit(coord: Coordinate, coord_parent: Coordinate):
        nonlocal visited

        # If the end is reached, we are done.
        # Add to "visited" along with parent for path tracing later.
        if coord.x == e.x and coord.y == e.y:
            visited[coord] = coord_parent
            return True

        adjacent = [
            Coordinate(max(0, coord.x - 1), coord.y),
            Coordinate(coord.x, max(0, coord.y - 1)),
            Coordinate(min(x_size, coord.x + 1), coord.y),
            Coordinate(coord.x, min(y_size, coord.y + 1))
        ]

        # Find available adjacent cells (cell is white and is not the cell itself).
        # "Cell itself" can result from the clamping logic above.
        available_adjacent = [c for c in adjacent if
                              maze[c.x][c.y] == WHITE and (c.x != coord.x or c.y != coord.y)]

        # Add each available adjacent cell to the BFS queue while recording its parent
        queue.extend(map(lambda x: ChildParent(child=x, parent=coord), available_adjacent))

        # Mark the cell as "BLACK" to avoid visiting it again
        maze[coord.x][coord.y] = BLACK

        # Record the cell in "visited", pointing to its parent for path tracing later
        visited[coord] = coord_parent

        return False

    # Start at the starting cell
    cell = s

    # The starting cell has no parent
    null_cell = Coordinate(-1, -1)
    queue.append(ChildParent(cell, null_cell))

    is_end_found = False
    # Stop if end has been found or the BFS queue has been exhausted
    while not is_end_found and queue:
        child_parent = queue.pop(0)

        is_end_found = _visit(child_parent.child, child_parent.parent)

    # If the end has been found, trace the visited node parents from the end and reverse to get the path
    # to the end from the start
    path = []
    if is_end_found:
        visited_node = e
        while visited_node != null_cell:
            path.append(visited_node)
            visited_node = visited[visited_node]
        path.reverse()

    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
