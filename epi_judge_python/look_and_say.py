from test_framework import generic_test

# Input:
# n: int, rep. nth integer in the look-and-say sequence

# Output:
# result: str, the nth integer in the seq. as a string

# Notes / Assumptions:
# - 2 digits generated for each group

# Example:
# 1
# 11
# 21
# 12 11
# 11 12 21
# 31 22 11

# Outline:

def look_and_say(n: int) -> str:
    prev_seq = ['1']

    if n <= 1:
        return prev_seq[0]

    new_seq = []
    for i in range(1, n):
        j = 0
        cur = prev_seq[j]
        count = 0
        new_seq = []
        while j < len(prev_seq):
            while j < len(prev_seq) and prev_seq[j] == cur:
                count += 1
                j += 1

            # TODO: Add to notes (be wary of creating new arrays vs just appending)
            new_seq.extend([str(count), cur])

            count = 0
            if j < len(prev_seq):
                cur = prev_seq[j]

        prev_seq = new_seq

    return ''.join(new_seq)

def look_and_say1(n: int) -> str:
    def next_number(s):
        result, i = [], 0

        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1

            result.append(str(count) + s[i])
            i += 1

        return ''.join(result)

    s = '1'
    for _ in range(1, n):
        s = next_number(s)

    return s

if __name__ == '__main__':
    #print(look_and_say(8))
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
