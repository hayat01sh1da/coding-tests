import pytest

from fibonacci import fibonacci


@pytest.mark.parametrize(
    ('start', 'count', 'expected'),
    [
        (0, 10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        (10, 10, [10, 11, 21, 32, 53, 85, 138, 223, 361, 584]),
    ],
)
def test_fibonacci(start: int, count: int, expected: list[int]) -> None:
    assert fibonacci(start, count) == expected
