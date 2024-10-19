require 'minitest/autorun'
require_relative '../src/application'

class LetterInspection::ApplicationTest < Minitest::Test
  def test_exactly_equal_size_and_included
    assert_equal true,  ::LetterInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar', target: 'abefghooor')
  end

  def test_partly_equal_size_and_included
    assert_equal false,  ::LetterInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar', target: 'hoge')
  end

  def test_not_equal_size_and_included
    assert_equal false,  ::LetterInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar', target: 'piyopoopee')
  end
end
