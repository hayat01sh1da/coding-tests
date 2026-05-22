def fizzbuzz_in_if(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        result = 'FizzBuzz'
    elif num % 3 == 0:
        result = 'Fizz'
    elif num % 5 == 0:
        result = 'Buzz'
    else:
        result = str(num)
    return result


def fizzbuzz_in_if_and_ternary(num: int) -> str:
    if num % 3 == 0:
        return 'FizzBuzz' if num % 5 == 0 else 'Fizz'
    else:
        return 'Buzz' if num % 5 == 0 else str(num)


def fizzbuzz_in_ternary(num: int) -> str:
    return ('FizzBuzz' if num % 5 == 0 else 'Fizz') if num % 3 == 0 \
        else ('Buzz' if num % 5 == 0 else str(num))
