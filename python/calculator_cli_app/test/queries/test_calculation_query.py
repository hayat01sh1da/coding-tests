from calculation_query import CalculationQuery


class CalculationQueryTest:
    def setup_method(self) -> None:
        self._calculation_query: CalculationQuery = CalculationQuery('foo')


class ArgumentZeroTest(CalculationQueryTest):
    def test_f(self) -> None:
        assert self._calculation_query.f(0) == 1


class ArgumentTwoTest(CalculationQueryTest):
    def test_f(self) -> None:
        assert self._calculation_query.f(2) == 2


class ArgumentFourTest(CalculationQueryTest):
    def test_f(self) -> None:
        assert self._calculation_query.f(4) == 348
