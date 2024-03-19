def __to_int_with_rescue__(n):
    try:
        return int(n)
    except ValueError:
        return 'Not Integer'
