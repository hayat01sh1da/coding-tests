import pytest

from fizzbuzz import fizzbuzz_in_if, fizzbuzz_in_ternary


def _expected(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)


@pytest.mark.parametrize('implementation', [fizzbuzz_in_if, fizzbuzz_in_ternary])
@pytest.mark.parametrize('num', range(1, 101))
def test_fizzbuzz(implementation, num):
    assert implementation(num) == _expected(num)
