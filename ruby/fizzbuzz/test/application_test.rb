require 'minitest/autorun'
require_relative '../src/application'

class ApplicationTest < Minitest::Test; end

class IfStatementTest < ApplicationTest
  def test_fizzbuzz
    1.upto(100).each do |num|
      if (num % 3).zero? && (num % 5).zero?
        assert_equal 'FizzBuzz', fizzbuzz_in_if(num)
      elsif (num % 3).zero?
        assert_equal 'Fizz', fizzbuzz_in_if(num)
      elsif (num % 5).zero?
        assert_equal 'Buzz', fizzbuzz_in_if(num)
      else
        assert_equal num.to_s, fizzbuzz_in_if(num)
      end
    end
  end
end

class TernaryStatementTest < ApplicationTest
  def test_fizzbuzz
    1.upto(100).each do |num|
      if (num % 3).zero? && (num % 5).zero?
        assert_equal 'FizzBuzz', fizzbuzz_in_ternary(num)
      elsif (num % 3).zero?
        assert_equal 'Fizz', fizzbuzz_in_ternary(num)
      elsif (num % 5).zero?
        assert_equal 'Buzz', fizzbuzz_in_ternary(num)
      else
        assert_equal num.to_s, fizzbuzz_in_ternary(num)
      end
    end
  end
end

class HybridStatementTest < ApplicationTest
  def test_fizzbuzz
    1.upto(100).each do |num|
      if (num % 3).zero? && (num % 5).zero?
        assert_equal 'FizzBuzz', fizzbuzz_in_if_and_ternary(num)
      elsif (num % 3).zero?
        assert_equal 'Fizz', fizzbuzz_in_if_and_ternary(num)
      elsif (num % 5).zero?
        assert_equal 'Buzz', fizzbuzz_in_if_and_ternary(num)
      else
        assert_equal num.to_s, fizzbuzz_in_if_and_ternary(num)
      end
    end
  end
end
