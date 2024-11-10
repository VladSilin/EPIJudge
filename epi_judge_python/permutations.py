from typing import List

from test_framework import generic_test, test_utils

# [3]: [[3]]
# [2, 3]: [[2, 3], [3, 2]]
# [1, 2, 3]: [[1, 2, 3], [2, 3, 1], [1, 3, 2], [3, 2, 1]]
# TODO: Add to notes (MAKE SURE YOU DO AN EXAMPLE especially if overwhelmed)

# TODO: Try the textbook way
# TODO: Try the way of putting the current element at every position in the permutations without that element
def permutations0(A: List[int]) -> List[List[int]]:
    result = []

    def _permutations(_A: List[int]):
        if len(_A) == 1:
            return [[_A[0]]]
        elif len(_A) == 0:
            return []

        local_result = []
        for p in _permutations(_A[1:]):
            for i in range(len(p) + 1):
                temp = p.copy()
                temp.insert(i, _A[0])
                local_result.append(temp)

        if len(_A) == len(A):
            result.extend(local_result)

        return local_result

    _permutations(A)

    return [[A[0]]] if len(A) == 1 else result


# [1, 2, 3]
#   1: [2, 3] -> [[1, 2, 3], [1, 3, 2]]
#     2: [3] -> [[2, 3]]
#       -> [[3]]
#     3: [2] -> [[2, 3], [3, 2]]
#       -> [[2]]
#   2: [1, 3] -> [[2, 1, 3], [2, 3, 1]]
#     1: [3] -> [[1, 3]]
#       -> [[3]]
#     3: [1] -> [[1, 3], [3, 1]]
#       -> [[1]]
#   3: [1, 2]
#     1: [2]
#       -> [[2]]
#     2: [1]
#       -> [[1]]
def permutations1(A: List[int]) -> List[List[int]]:
    def _permutations(_A: List[int]):
        if len(_A) < 2:
            return [_A]

        # TODO: Add to notes (initializing a local variable and returning it (message passing across the stack))
        result = []
        for i in range(len(_A)):
            list_without_element_at_i = _A[:i] + _A[i + 1:]

            ps = _permutations(list_without_element_at_i)

            for p in ps:
                result.append([_A[i]] + p)

        return result

    return _permutations(A)


def permutations(A: List[int]) -> List[List[int]]:
    result = []

    # TODO: Add to notes (keep in mind the "vectors of change", e.g. recursion iteration vs for loop iteration
    # how they interact, and what each achieves in moving towards the goal/base case)
    def _permutations(swap_subject_index: int):
        if swap_subject_index == len(A) - 1:
            result.append(A.copy())
            return

        for j in range(swap_subject_index, len(A)):
            A[swap_subject_index], A[j] = A[j], A[swap_subject_index]
            _permutations(swap_subject_index + 1)
            A[swap_subject_index], A[j] = A[j], A[swap_subject_index]

    _permutations(0)
    return result


if __name__ == '__main__':
    #r = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    #print(r)
    #test = [1, 2, 3]
    #print(test[:2] + test[3:])
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations1,
                                       test_utils.unordered_compare))
