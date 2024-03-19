import { CalculationQuery } from './queies/calculation_query';
import { validate } from './validations/args_validation';

const Application = class {
  constructor(args) {
    this.args_size        = args.length;
    this.seed             = args[0];
    this.n                = args[args.length -1];
    this.calculation_query = null;
  }

  run() {
    validate(this.args_size, this.seed, parseInt(this.n));

    const result = this.__calculation_query__().f(parseInt(this.n));
    console.log(result);
  }

  // private

  __calculation_query__() {
    if (this.__calculation_query__ === null) {
      this.__calculation_query__ = new CalculationQuery(this.seed);
      return this.__calculation_query__;
    } else {
      return this.__calculation_query__;
    }
  }
}

export {
  Application
};
