from collections.abc import Callable

import pytest

from fizzbuzz import fizzbuzz_in_if, fizzbuzz_in_ternary


def _expected(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)


@pytest.mark.parametrize('implementation',
                         [fizzbuzz_in_if, fizzbuzz_in_ternary])
@pytest.mark.parametrize('num', range(1, 101))
def test_fizzbuzz(implementation: Callable[[int], str], num: int) -> None:
    assert implementation(num) == _expected(num)
