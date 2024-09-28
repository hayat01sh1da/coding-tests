require 'minitest/autorun'
require_relative '../src/fizzbuzz'

class FizzBuzzTest < Minitest::Test; end

class IfStatementTest < FizzBuzzTest
  def test_fizzbuzz
    1.upto(100).each do |num|
      if num % 3 == 0 && num % 5 == 0
        assert_equal 'FizzBuzz', fizzbuzz_in_if(num)
      elsif num % 3 == 0
        assert_equal 'Fizz', fizzbuzz_in_if(num)
      elsif num % 5 == 0
        assert_equal 'Buzz', fizzbuzz_in_if(num)
      else
        assert_equal num.to_s, fizzbuzz_in_if(num)
      end
    end
  end
end

class TernaryStatementTest < FizzBuzzTest
  def test_fizzbuzz
    1.upto(100).each do |num|
      if num % 3 == 0 && num % 5 == 0
        assert_equal 'FizzBuzz', fizzbuzz_in_ternary(num)
      elsif num % 3 == 0
        assert_equal 'Fizz', fizzbuzz_in_ternary(num)
      elsif num % 5 == 0
        assert_equal 'Buzz', fizzbuzz_in_ternary(num)
      else
        assert_equal num.to_s, fizzbuzz_in_ternary(num)
      end
    end
  end
end

class HybridStatementTest < FizzBuzzTest
  def test_fizzbuzz
    1.upto(100).each do |num|
      if num % 3 == 0 && num % 5 == 0
        assert_equal 'FizzBuzz', fizzbuzz_in_if_and_ternary(num)
      elsif num % 3 == 0
        assert_equal 'Fizz', fizzbuzz_in_if_and_ternary(num)
      elsif num % 5 == 0
        assert_equal 'Buzz', fizzbuzz_in_if_and_ternary(num)
      else
        assert_equal num.to_s, fizzbuzz_in_if_and_ternary(num)
      end
    end
  end
end
