require 'minitest/autorun'
require_relative '../../src/queries/calculation_query'

class CalculationQueryTest < Minitest::Test
  def setup
    @calculation_query = ::Queries::CalculationQuery.new('foo')
  end

  private

  attr_reader :calculation_query
end

class ArgumentZeroTest < CalculationQueryTest
  def test_f
    assert_equal(1, calculation_query.f(0))
  end
end

class ArgumentTwoTest < CalculationQueryTest
  def test_f
    assert_equal(2, calculation_query.f(2))
  end
end

class ArgumentFourTest < CalculationQueryTest
  def test_f
    assert_equal(348, calculation_query.f(4))
  end
end
