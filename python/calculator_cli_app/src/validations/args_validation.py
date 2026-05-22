class ArgsValidation:
    def validate(
            self,
            args_size: int,
            seed: str | None,
            n: int | None) -> None:
        if args_size > 2:
            print('Too many arguments')
            exit(1)
        elif args_size == 0:
            print('No argument provided')
            exit(1)
        elif args_size == 1:
            print('Provide both seed and n')
            exit(1)
        elif not isinstance(seed, str) or n is None:
            print('Provide seed as string and n as number')
            exit(1)
