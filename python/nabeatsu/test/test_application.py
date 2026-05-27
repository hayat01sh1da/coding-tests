from collections.abc import Callable

from application import go_crazy_in_if, go_crazy_in_ternary


def _expected_for(num: int) -> str:
    if num % 3 == 0 or '3' in str(num):
        return f'{num}!'
    return str(num)


def _assert_go_crazy_sequence(impl: Callable[[int], str]) -> None:
    for num in range(1, 41):
        assert impl(num) == _expected_for(num)


def test_go_crazy_in_if_statement() -> None:
    _assert_go_crazy_sequence(go_crazy_in_if)


def test_go_crazy_in_ternary_statement() -> None:
    _assert_go_crazy_sequence(go_crazy_in_ternary)
