def __validate__(args_size, seed, n):
    if args_size > 2:
        print('Too many arguments')
        exit(1)
    elif args_size == 0:
        print('No argument provided')
        exit(1)
    elif args_size == 1:
        print('Provide both seed and n')
        exit(1)
    elif type(seed) != str or n == 'Not Integer':
        print('Provide seed as string and n as number')
        exit(1)
