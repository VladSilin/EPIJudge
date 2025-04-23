from test_framework import generic_test

# Input:
# s: str, a string containing {,},(,),[,]

# Output:
# is_well_formed: bool, do all the parens. match?

# Notes / Assumptions:

# Example:
# [()[]{()()}]
#
# [[(]

# Outline:
def is_well_formed(s: str) -> bool:
    open_to_close_map = {
        '{': '}',
        '(': ')',
        '[': ']',
    }

    stack = []
    for c in s:
        if c in open_to_close_map:
            stack.append(c)
        else:
            if not stack or open_to_close_map[stack.pop()] != c:
                return False

    return not stack


if __name__ == '__main__':
    #test = '[()[]{())}'

    #well_formed = is_well_formed(test)

    #print(well_formed)

    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
