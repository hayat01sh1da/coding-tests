# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def test_fizzbuzz_in_if
    assert_fizzbuzz_sequence(:fizzbuzz_in_if)
  end

  def test_fizzbuzz_in_ternary
    assert_fizzbuzz_sequence(:fizzbuzz_in_ternary)
  end

  def test_fizzbuzz_in_if_and_ternary
    assert_fizzbuzz_sequence(:fizzbuzz_in_if_and_ternary)
  end

  private

  def assert_fizzbuzz_sequence(impl)
    1.upto(100).each do |num|
      assert_equal expected_for(num), send(impl, num)
    end
  end

  def expected_for(num)
    return 'FizzBuzz' if (num % 15).zero?
    return 'Fizz'     if (num % 3).zero?
    return 'Buzz'     if (num % 5).zero?

    num.to_s
  end
end
