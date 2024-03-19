require_relative './queries/calculation_query'
require_relative './validations/args_validation'

module CalculatorCliApp
  class Application
    include ::Validations::ArgsValidation

    def initialize(args)
      @args_size = args.size
      @seed      = args.first
      @n         = args.last
    end

    def run
      validate!(args_size, seed, n.to_i.nonzero?)

      result = calulation_query.f(n)
      puts result
    end

    private

    attr_reader :args_size, :seed, :n

    def calulation_query
      @calulation_query ||= ::Queries::CalculationQuery.new(seed)
    end
  end
end
