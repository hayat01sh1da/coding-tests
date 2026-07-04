"""Tests the query that performs the arithmetic for the calculator CLI app."""

import pytest

from calculation_query import CalculationQuery


@pytest.fixture
def calculation_query() -> CalculationQuery:
    return CalculationQuery('foo')


def test_f_returns_one_when_argument_is_zero(
        calculation_query: CalculationQuery) -> None:
    assert calculation_query.f(0) == 1


def test_f_returns_two_when_argument_is_two(
        calculation_query: CalculationQuery) -> None:
    assert calculation_query.f(2) == 2


def test_f_recurses_for_an_even_argument(
        calculation_query: CalculationQuery) -> None:
    assert calculation_query.f(4) == 348
