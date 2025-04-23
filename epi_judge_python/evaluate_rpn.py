from test_framework import generic_test

# Input:
# expression: str, a string containing an expr. in RPN

# Output:

# Notes / Assumptions:
# - Each "token" is a function call
# - Tokens can be:
#   - Arg() -> self
#   - Fn(Arg, Arg, op)

# Example:
# "3,4,+, 2,x, 1,+"
# - Each "token" is a function call
# - Tokens can be:
#   - Arg() -> self
#   - Fn(Arg, Arg, op)

# Outline:
# - Split on commas
# - Go through the tokens:
#   - Put each token on the stack
#   - If operator, pop 2 entries from the stack and eval the operator
#   - Place result back on the stack
def evaluate(expression: str) -> int:
    if expression == '':
        return 0

    split_expr = expression.split(',')

    stack = []
    op_map = {
        '+': lambda n1, n2: n1 + n2,
        '-': lambda n1, n2: n2 - n1,
        'x': lambda n1, n2: n1 * n2,
        '*': lambda n1, n2: n1 * n2,
        '/': lambda n1, n2: int(n2 / n1),
    }
    for c in split_expr:
        if c in op_map:
            arg1, arg2 = stack.pop(), stack.pop()
            result = op_map[c](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(c))

    return stack[-1]


if __name__ == '__main__':
    #test = "11,8,10,*,+,7,12,*,+,12,7,*,+,9,14,*,+,17,+"
    ##test = ""

    #r = evaluate(test)
    #print(r)

    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
