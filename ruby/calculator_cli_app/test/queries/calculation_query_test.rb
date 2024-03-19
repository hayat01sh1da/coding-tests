require 'minitest/autorun'
require_relative '../../src/queries/calculation_query'

class CalculationQueryTest < Minitest::Test
  def setup
    @calculation_query = ::Queries::CalculationQuery.new('foo')
  end

  def test_f_with_zero
    assert_equal(1, @calculation_query.f(0))
  end

  def test_f_with_two
    assert_equal(2, @calculation_query.f(2))
  end

  def test_f_with_four
    assert_equal(348, @calculation_query.f(4))
  end
end
