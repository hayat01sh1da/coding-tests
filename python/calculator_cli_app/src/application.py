import sys
sys.path.append('./calculator_cli_app/src')
sys.path.append('./calculator_cli_app/src/lib')
sys.path.append('./calculator_cli_app/src/queries')
sys.path.append('./calculator_cli_app/src/validations')
from data_type_conversion import __to_int_with_rescue__
from calculation_query import CalculationQuery
from args_validation import __validate__

class Application:
    def __init__(self, args):
        self.args_size = len(args)
        if self.args_size > 0:
            self.seed = args[0]
            self.n    = args[-1]
        else:
            self.seed = ''
            self.n    = ''
        self.calculation_query = CalculationQuery(self.seed)

    def run(self):
        __validate__(self.args_size, self.seed, __to_int_with_rescue__(self.n))

        result = self.calculation_query.f(__to_int_with_rescue__(self.n))
        print(result)
