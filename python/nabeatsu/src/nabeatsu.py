def go_crazy_in_if(num):
    if num % 3 == 0 or '3' in str(num):
        # Express the status of 'crazy' with '!'
        result = str(num) + '!'
    else:
        result = str(num)
    return result

def go_crazy_in_ternary(num):
    # Express the status of 'crazy' with '!'
    result = str(num) + '!' if num % 3 == 0 or '3' in str(num) else str(num)
    return result
