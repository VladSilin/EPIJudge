import functools
from typing import List
from collections import namedtuple

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# Given:
#   miles_per_gallon = 20
#   distances_to_next_city: List[int]
#       total_road_distance = sum(distances_bw_cities)
#   gallons: List[i]
#
# Return:
#   ample_city
#       city such that can do a full cycle without running out of gas
#
# Brute Force:
# - For each city x:
#   - while not back at city x
#       - Add the city gas
#       - Subtract the (city distance / MPG)

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
#
# Example:
# gallons:   [50, 20, 5, 30, 25, 10, 10]
# distances: [900, 600, 200, 400, 600, 200, 100]
def find_ample_city0(gallons: List[int], distances: List[int]) -> int:
    # TODO: Add to notes (when iterating through more than one collection, index is more useful than for-each)
    for i in range(len(distances)):
        j = i
        # TODO: Add to notes (keep track of STATE you may need to reset, e.g. per outer loop cycle)
        tank = 0
        while tank >= 0:
            tank += gallons[j]
            # TODO: Add to notes (when running into unexpected bugs, look back at problem breakdown (* MPG was missed
            #   here and you were stuck, but was there in the description above)
            # TODO: Add to notes (remember about integer division)
            tank -= distances[j] // MPG

            if tank < 0:
                break

            j = j + 1 if j + 1 < len(distances) else 0

            if j == i:
                return j


# TODO: Add to notes (consider graphing when problem involves rates of change)
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    remaining_gallons = 0
    CityAndRemainingGas = namedtuple('CityAndRemainingGas', ('city', 'remaining_gallons'))

    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)

    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - (distances[i - 1] // MPG)
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons)

    return city_remaining_gallons_pair.city


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    #gallons = [50, 20, 5, 30, 25, 10, 10]
    #distances = [900, 600, 200, 400, 600, 200, 100]

    #result = find_ample_city(gallons, distances)
    #print(result)

    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
