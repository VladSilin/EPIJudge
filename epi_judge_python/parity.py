from test_framework import generic_test


def parity(x: int) -> int:
    num_ones = 0
    bit_mask = 1

    while x:
        if (x & bit_mask) == 1:
            num_ones += 1

        x >>= 1

    return num_ones % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
