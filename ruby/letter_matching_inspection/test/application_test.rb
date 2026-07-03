# frozen_string_literal: true

require 'minitest/autorun'
require_relative '../src/application'

module LetterMatchingInspection
  # Tests the letter-matching inspection application.
  class ApplicationTest < Minitest::Test
    def test_exactly_equal_size_and_included
      assert ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
                                                                                      target: 'abefghooor')
    end

    def test_partly_equal_size_and_included
      refute ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
                                                                                      target: 'hoge')
    end

    def test_not_equal_size_and_included
      refute ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
                                                                                      target: 'piyopoopee')
    end
  end
end
