from application import fibonacci


def test_fibonacci_from_zero() -> None:
    assert fibonacci(init_num=0, iter=10) == \
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_from_ten() -> None:
    assert fibonacci(init_num=10, iter=10) == \
        [10, 11, 21, 32, 53, 85, 138, 223, 361, 584]
