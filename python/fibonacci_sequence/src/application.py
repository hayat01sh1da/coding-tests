def fibonacci(*, init_num: int, iter: int) -> list[int]:
    current_num = init_num
    next_num = current_num + 1
    result: list[int] = []
    for _ in range(iter):
        result_num = current_num
        current_num, next_num = next_num, current_num + next_num
        result.append(result_num)
    return result
