def fibonacci(init_num, iter):
    current_num = init_num
    next_num    = current_num + 1
    result      = list()
    for num in range(init_num, iter + init_num):
        result.append(current_num)
        current_num, next_num = next_num, current_num + next_num
    return result
