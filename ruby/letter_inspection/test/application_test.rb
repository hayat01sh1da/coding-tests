require 'minitest/autorun'
require_relative '../src/application'

class LetterInspection::ApplicationTest < Minitest::Test
  def setup
    str_1      = 'hogefoobar'
    str_2      = 'abefghooor'
    str_3      = 'hoge'
    str_4      = 'piyopoopee'
    @pattern_1 = ::LetterInspection::Application.new(str_1, str_2)
    @pattern_2 = ::LetterInspection::Application.new(str_1, str_3)
    @pattern_3 = ::LetterInspection::Application.new(str_1, str_4)
  end

  private

  attr_reader :pattern_1, :pattern_2, :pattern_3
end

class RegularCaseTest < LetterInspection::ApplicationTest
  def test_exactly_equal_size_and_included_1
    assert_equal true,  pattern_1.exactly_equal_size_and_included?
  end
end

class IrregularCaseTest < LetterInspection::ApplicationTest; end

class TestCase1 < IrregularCaseTest
  def test_exactly_equal_size_and_included_2
    assert_equal false, pattern_2.exactly_equal_size_and_included?
  end
end

class TestCase2 < IrregularCaseTest
  def test_exactly_equal_size_and_included_3
    assert_equal false, pattern_3.exactly_equal_size_and_included?
  end
end
