import math
from typing import List

from test_framework import generic_test


def matrix_in_spiral_order_mess(square_matrix: List[List[int]]) -> List[int]:
    def iterate_right(cur_loc: (int, int)) -> (int, int):
        # print('visited', visited)
        # print('start_right', cur_loc)
        # print('iterate_right')
        temp_loc = cur_loc
        next_loc = (temp_loc[0], temp_loc[1] + 1)
        while temp_loc[1] < len(square_matrix) - 1 and next_loc not in visited:
            print(square_matrix[temp_loc[0]][temp_loc[1]])
            # print(temp_loc)
            visited.add(temp_loc)
            temp_loc = next_loc
            next_loc = (temp_loc[0], temp_loc[1] + 1)

        return temp_loc

    def iterate_down(cur_loc: (int, int)) -> (int, int):
        # print('visited', visited)
        # print('start_down', cur_loc)
        # print('iterate_down')
        temp_loc = cur_loc
        next_loc = (temp_loc[0] + 1, temp_loc[1])
        while temp_loc[0] < len(square_matrix) - 1 and next_loc not in visited:
            print(square_matrix[temp_loc[0]][temp_loc[1]])
            visited.add(temp_loc)
            temp_loc = next_loc
            next_loc = (temp_loc[0] + 1, temp_loc[1])

        return temp_loc

    def iterate_left(cur_loc: (int, int)) -> (int, int):
        # print('visited', visited)
        # print('start_left', cur_loc)
        # print('iterate_left')
        temp_loc = cur_loc
        next_loc = (temp_loc[0], temp_loc[1] - 1)
        while temp_loc[1] > 0 and next_loc not in visited:
            print(square_matrix[temp_loc[0]][temp_loc[1]])
            visited.add(temp_loc)
            temp_loc = next_loc
            next_loc = (temp_loc[0], temp_loc[1] - 1)

        return temp_loc

    def iterate_up(cur_loc: (int, int)) -> (int, int):
        # print('visited', visited)
        # print('start_up', cur_loc)
        # print('iterate_up')
        temp_loc = cur_loc
        next_loc = (temp_loc[0] - 1, temp_loc[1])
        while temp_loc[0] > 0 and next_loc not in visited:
            print(square_matrix[temp_loc[0]][temp_loc[1]])
            visited.add(temp_loc)
            temp_loc = next_loc
            next_loc = (temp_loc[0] - 1, temp_loc[1])

        return temp_loc

    op_order = [iterate_right, iterate_down, iterate_left, iterate_up]

    result = []

    visited = set()
    cur_index = (0, 0)
    op = 0

    # next_index = op_order[op](cur_index)
    while len(visited) < len(square_matrix) ** 2:
        cur_index = op_order[op](cur_index)

        op = 0 if op == len(op_order) - 1 else op + 1

        if op == 0:
            break

    return result


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    def _matrix_in_spiral_order(layer_offset: int):
        size = len(square_matrix)

        if size == 0 or len(square_matrix[0]) == 0:
            return
        elif size - layer_offset == 1 and size % 2 == 1:
            result.append(square_matrix[size // 2][size // 2])
            return
        elif size - layer_offset == 0:
            return

        o = layer_offset

        row_right = square_matrix[o][o:size - 1 - o]
        col_down = list(zip(*square_matrix))[size - 1 - o][o:size - 1 - o]
        row_left = square_matrix[size - 1 - o][size - 1 - o:o:-1]
        # TODO: Add to notes (could write the below line as list(zip(*square_matrix))[o][-1 - o:o:-1])
        col_up = list(zip(*square_matrix))[o][size - 1 - o:o:-1]

        result.extend(row_right)
        result.extend(col_down)
        result.extend(row_left)
        result.extend(col_up)

        _matrix_in_spiral_order(layer_offset + 1)

    result = []
    _matrix_in_spiral_order(0)

    return result


if __name__ == '__main__':
    # r1 = matrix_in_spiral_order([[4, 2, 7, 8],
    #                              [3, 1, 8, 3],
    #                              [9, 5, 6, 9],
    #                              [7, 2, 1, 5]])
    #
    # r2 = matrix_in_spiral_order([[4, 2, 7],
    #                              [3, 1, 8],
    #                              [9, 5, 6]])
    #
    # r3 = matrix_in_spiral_order([[4, 2],
    #                              [3, 1]])
    #
    # r4 = matrix_in_spiral_order([[4]])
    #
    # r5 = matrix_in_spiral_order([[]])
    #
    # print(r1)
    # print(r2)
    # print(r3)
    # print(r4)
    # print(r5)

    exit(
       generic_test.generic_test_main('spiral_ordering.py',
                                      'spiral_ordering.tsv',
                                      matrix_in_spiral_order))
