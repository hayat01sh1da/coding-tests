require 'minitest/autorun'
require_relative '../src/fibonacci'

class FibonacciTest < Minitest::Test
  def test_fibonacci_1
    assert_equal(
      [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
      fibonacci(init_num: 0, iter: 10)
    )
  end

  def test_fibonacci_2
    assert_equal(
      [10, 11, 21, 32, 53, 85, 138, 223, 361, 584],
      fibonacci(init_num: 10, iter: 10)
    )
  end
end
