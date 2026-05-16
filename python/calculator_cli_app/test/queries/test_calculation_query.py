import pytest

from calculation_query import CalculationQuery


@pytest.mark.parametrize(
    ('argument', 'expected'),
    [
        (0, 1),
        (2, 2),
        (4, 348),
    ],
)
def test_f(argument, expected):
    assert CalculationQuery('foo').f(argument) == expected
