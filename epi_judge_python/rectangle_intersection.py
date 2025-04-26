import collections
from email.contentmanager import set_message_content

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple("Rect", ("x", "y", "width", "height"))

# Input:
# r1: Rect(x, y, w, h), rect. 1
# r2: Rect(x, y, w, h), rect. 2

# Output:
# r_int: Rect(x, y, w, h) formed by their intersection

# Notes / Assumptions:
# - Points are discreet

# Example:

# Outline:
# - Find smaller rectangle
# - Go through x to x + w, add all points
# - Go through y to y + h, add all points
# - Go through other corner x
# - Go through other corner y
# - Add all tuples to a set
# - Do the same for other rect, for each point:
#   - If in set, save

# - If 4 points, for x, y, w, h from 4 points
# - If 2 points, compute other 2 points and form x, y, w, h
def intersect_rectangle0(r1: Rect, r2: Rect) -> Rect:
    a1, a2 = r1.width * r1.height, r2.width * r2.height

    # r1 is now the smaller one
    if a1 > a2:
        r1, r2 = r2, r1

    def get_all_rect_points(r):
        rect_points = set([(r.x + i, r.y) for i in range(r.width)])
        rect_points = rect_points.union(set([(r.x, r.y + i) for i in range(r.height)]))
        rect_points = rect_points.union(
            set([(r.x + i, r.y + r.height) for i in range(r.width)])
        )
        rect_points = rect_points.union(
            set([(r.x + r.width, r.y + i) for i in range(r.height)])
        )

        return rect_points

    common_points = get_all_rect_points(r1).intersection(get_all_rect_points(r2))
    sorted_points = sorted(common_points)

    x = min(
        sorted_points[0][0],
        sorted_points[1][0],
        sorted_points[2][0],
        sorted_points[3][0],
    )
    y = min(
        sorted_points[0][1],
        sorted_points[1][1],
        sorted_points[2][1],
        sorted_points[3][1],
    )
    w = abs(sorted_points[0][0] - sorted_points[2][0])
    h = abs(sorted_points[0][1] - sorted_points[1][1])
    print(sorted_points)

    return Rect(x, y, w, h)


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def is_intersecting(R1, R2):
        return (
            R1.x <= R2.x + R2.width
            and R1.x + R1.width >= R2.x
            and R1.y <= R2.y + R2.height
            and R1.y + R1.height >= R2.y
        )

    if not is_intersecting(r1, r2):
        return Rect(0, 0, -1, -1)

    return Rect(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        max(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y),
    )


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    # rect1 = Rect(0, 1, 4, 5)
    # rect2 = Rect(1, 0, 2, 7)
    #
    # res = intersect_rectangle(rect1, rect2)
    # print(res)
    #
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            "rectangle_intersection.tsv",
            intersect_rectangle_wrapper,
            res_printer=res_printer,
        )
    )
