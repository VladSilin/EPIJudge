from test_framework import generic_test


def power2(x: float, y: int) -> float:
    result = 1
    for _ in range(1, abs(y) + 1):
        result *= (x if y > 0 else 1 / x)

    return result


def power(x: float, y: int) -> float:
    exp = y

    if y < 0:
        x, exp = 1 / x, -exp

    if exp == 0:
        return 1

    halved_exp_result = power(x, exp >> 1)

    return halved_exp_result * halved_exp_result * x if exp & 1 else halved_exp_result * halved_exp_result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
