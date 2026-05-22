from args_validation import ArgsValidation
from calculation_query import CalculationQuery


class Application(ArgsValidation):
    @classmethod
    def run(cls, args: list[str]) -> None:
        cls(args)._run()

    def __init__(self, args: list[str]) -> None:
        self._args_size: int = len(args)
        self._seed: str | None = args[0] if args else None
        self._n: str | None = args[-1] if args else None

    def _run(self) -> None:
        n = self._n_to_int_nonzero()
        self.validate(self._args_size, self._seed, n)
        assert n is not None
        print(self._calculation_query.f(n))

    # private

    def _n_to_int_nonzero(self) -> int | None:
        try:
            value = int(self._n) if self._n is not None else None
        except (ValueError, TypeError):
            return None
        return value if value else None

    @property
    def _calculation_query(self) -> CalculationQuery:
        if not hasattr(self, '_cached_calculation_query'):
            self._cached_calculation_query: CalculationQuery = \
                CalculationQuery(self._seed or '')
        return self._cached_calculation_query
