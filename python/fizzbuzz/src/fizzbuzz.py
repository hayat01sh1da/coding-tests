def fizzbuzz_in_if(num):
    if num % 3 == 0 and num % 5 == 0:
        result = 'FizzBuzz'
    elif num % 3 == 0:
        result = 'Fizz'
    elif num % 5 == 0:
        result = 'Buzz'
    else:
        result = str(num)
    return result

def fizzbuzz_in_ternary(num):
    result = 'FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else str(num)
    return result
