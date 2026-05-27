from collections.abc import Callable

from application import (
    fizzbuzz_in_if,
    fizzbuzz_in_if_and_ternary,
    fizzbuzz_in_ternary,
)


def _expected_for(num: int) -> str:
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)


def _assert_fizzbuzz_sequence(impl: Callable[[int], str]) -> None:
    for num in range(1, 101):
        assert impl(num) == _expected_for(num)


def test_fizzbuzz_in_if() -> None:
    _assert_fizzbuzz_sequence(fizzbuzz_in_if)


def test_fizzbuzz_in_ternary() -> None:
    _assert_fizzbuzz_sequence(fizzbuzz_in_ternary)


def test_fizzbuzz_in_if_and_ternary() -> None:
    _assert_fizzbuzz_sequence(fizzbuzz_in_if_and_ternary)
