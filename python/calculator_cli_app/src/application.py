from args_validation import __validate__
from calculation_query import CalculationQuery
from data_type_conversion import __to_int_with_rescue__
from typing import cast
import sys
sys.path.append('./calculator_cli_app/src')
sys.path.append('./calculator_cli_app/src/lib')
sys.path.append('./calculator_cli_app/src/queries')
sys.path.append('./calculator_cli_app/src/validations')


class Application:
    def __init__(self, args: list[str]) -> None:
        self.args_size: int = len(args)
        if self.args_size > 0:
            self.seed: str = args[0]
            self.n: str = args[-1]
        else:
            self.seed = ''
            self.n = ''
        self.calculation_query: CalculationQuery = CalculationQuery(self.seed)

    def run(self) -> None:
        __validate__(self.args_size, self.seed, __to_int_with_rescue__(self.n))

        result = self.calculation_query.f(
            cast(int, __to_int_with_rescue__(self.n)))
        print(result)
