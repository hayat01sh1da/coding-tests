from collections.abc import Callable

import pytest

from nabeatsu import go_crazy_in_if, go_crazy_in_ternary


def _expected(num: int) -> str:
    return f'{num}!' if num % 3 == 0 or '3' in str(num) else str(num)


@pytest.mark.parametrize('implementation',
                         [go_crazy_in_if, go_crazy_in_ternary])
@pytest.mark.parametrize('num', range(1, 41))
def test_go_crazy(implementation: Callable[[int], str], num: int) -> None:
    assert implementation(num) == _expected(num)
