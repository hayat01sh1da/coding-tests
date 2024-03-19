require 'minitest/autorun'
require_relative '../src/nabeatsu'

class NabeatsuTest < Minitest::Test
  def test_go_crazy_in_if
    1.upto(40).each do |num|
      if num % 3 == 0 || num.to_s.include?('3')
        assert_equal "#{num.to_s}!", go_crazy_in_if(num)
      else
        assert_equal num.to_s, go_crazy_in_if(num)
      end
    end
  end

  def test_go_crazy_in_ternary
    1.upto(40).each do |num|
      if num % 3 == 0 || num.to_s.include?('3')
        assert_equal "#{num.to_s}!", go_crazy_in_ternary(num)
      else
        assert_equal num.to_s, go_crazy_in_ternary(num)
      end
    end
  end
end
