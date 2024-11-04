from test_framework import generic_test

# goal: 8
# result: 2 ^ 2


# TODO: Add to notes (to see if binary search is viable, see if
#  *eliminating an element implies that other elements can be eliminated*)
def square_root0(k: int) -> int:
    num = 0
    square = num ** 2

    while square <= k:
        num += 1
        square = num ** 2

    return num - 1


def square_root(k: int) -> int:
    start, end = 0, k

    # TODO: Add to notes (fiddly binary search index stuff)
    while start <= end:
        mid = (start + end) // 2
        square = mid * mid

        if square <= k:
            start = mid + 1
        else:
            end = mid - 1

    return start - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
