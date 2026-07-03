# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require_relative '../src/application'

# Tests every Nabeatsu implementation variant.
class ApplicationTest < Minitest::Test
  def test_go_crazy_in_if_statement
    1.upto(40).each do |num|
      if (num % 3).zero? || num.to_s.include?('3')
        assert_equal "#{num}!", go_crazy_in_if(num)
      else
        assert_equal num.to_s, go_crazy_in_if(num)
      end
    end
  end

  def test_go_crazy_in_ternary_statement
    1.upto(40).each do |num|
      if (num % 3).zero? || num.to_s.include?('3')
        assert_equal "#{num}!", go_crazy_in_ternary(num)
      else
        assert_equal num.to_s, go_crazy_in_ternary(num)
      end
    end
  end
end
