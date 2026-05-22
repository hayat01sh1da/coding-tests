from application import (
    fizzbuzz_in_if,
    fizzbuzz_in_if_and_ternary,
    fizzbuzz_in_ternary,
)


class ApplicationTest:
    pass


class IfStatementTest(ApplicationTest):
    def test_fizzbuzz(self) -> None:
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                assert fizzbuzz_in_if(num) == 'FizzBuzz'
            elif num % 3 == 0:
                assert fizzbuzz_in_if(num) == 'Fizz'
            elif num % 5 == 0:
                assert fizzbuzz_in_if(num) == 'Buzz'
            else:
                assert fizzbuzz_in_if(num) == str(num)


class TernaryStatementTest(ApplicationTest):
    def test_fizzbuzz(self) -> None:
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                assert fizzbuzz_in_ternary(num) == 'FizzBuzz'
            elif num % 3 == 0:
                assert fizzbuzz_in_ternary(num) == 'Fizz'
            elif num % 5 == 0:
                assert fizzbuzz_in_ternary(num) == 'Buzz'
            else:
                assert fizzbuzz_in_ternary(num) == str(num)


class HybridStatementTest(ApplicationTest):
    def test_fizzbuzz(self) -> None:
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                assert fizzbuzz_in_if_and_ternary(num) == 'FizzBuzz'
            elif num % 3 == 0:
                assert fizzbuzz_in_if_and_ternary(num) == 'Fizz'
            elif num % 5 == 0:
                assert fizzbuzz_in_if_and_ternary(num) == 'Buzz'
            else:
                assert fizzbuzz_in_if_and_ternary(num) == str(num)
