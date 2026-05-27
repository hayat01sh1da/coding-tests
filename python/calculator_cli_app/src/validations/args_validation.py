import sys


class ArgsValidation:
    """Argument-shape checks for Application; intended to be mixed in."""

    def validate(self, args_size: int, seed: str | None,
                 n: int | None) -> None:
        message = self._validation_error(args_size, seed, n)
        if message is None:
            return
        print(message)
        sys.exit(1)

    # private

    def _validation_error(self, args_size: int, seed: str | None,
                          n: int | None) -> str | None:
        if args_size > 2:
            return 'Too many arguments'
        if args_size == 0:
            return 'No argument provided'
        if args_size == 1:
            return 'Provide both seed and n'
        if not isinstance(seed, str) or n is None:
            return 'Provide seed as string and n as number'
        return None
