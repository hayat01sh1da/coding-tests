require 'minitest/autorun'
require_relative '../src/fibonacci'

class FibonacciTest < Minitest::Test; end

class TestCase1 < FibonacciTest
  def test_fibonacci
    assert_equal(
      [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
      fibonacci(init_num: 0, iter: 10)
    )
  end
end

class TestCase2 < FibonacciTest
  def test_fibonacci
    assert_equal(
      [10, 11, 21, 32, 53, 85, 138, 223, 361, 584],
      fibonacci(init_num: 10, iter: 10)
    )
  end
end
