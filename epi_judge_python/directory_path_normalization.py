from test_framework import generic_test

# Input:
# path: str, a pathname consisting of filenames, /, ., ..

# Output:
# shortest_eq_path: str, the shortest possible path

# Notes / Assumptions:
# - Tokens:
#   - '/', '.', '..'
# - Assume path is well-formed at first

# Example:
# /usr/bin/gcc
#
# /usr/lib/../bin/gcc
# usr, lib, .., bin, gcc

# Outline:
# - Split on '/'
# - Peek — if not token, then:
#   - For '/', ignore
#   - For '.', ignore
#   - For '..', pop off the stack
def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError('Empty string is not a valid path')

    split = path.split('/')
    ignore = {'.', ''}

    stack = [path[0]] if path[0] == '/' else []
    for part in split:
        if part in ignore:
            continue

        if part == '..':
            # NOTE: The case where there are multiple subsequent '..' (more than there are elements to pop)
            if not stack or stack[-1] == '..':
                stack.append(part)
            else:
                if stack[-1] == '/':
                    raise ValueError('Path error, cannot go back from \'/\'')
                stack.pop()
            continue

        stack.append(part)

    result = '/'.join(stack)
    return result[result.startswith('//'):]


if __name__ == '__main__':
    #test = '/'
    #result = shortest_equivalent_path(test)
    #print(result)

    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
