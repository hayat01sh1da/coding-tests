# rbs_inline: enabled

require_relative './queries/calculation_query'
require_relative './validations/args_validation'

module CalculatorCliApp
  class Application
    include ::Validations::ArgsValidation

    # @rbs args: Array[String]
    # @rbs return: void
    def initialize(args)
      @args_size = args.length
      @seed      = args.first
      @n         = args.last
    end

    # @rbs return: void
    def run
      validate!(args_size, seed, n.to_i.nonzero?)

      result = calculation_query.f(n)
      puts result
    end

    private

    attr_reader :args_size, :seed, :n

    # @rbs return: Queries::CalculationQuery
    def calculation_query
      @calculation_query ||= ::Queries::CalculationQuery.new(seed)
    end
  end
end
