# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require_relative '../src/application'

module CalculatorCliApp
  class ApplicationTest < Minitest::Test
    def setup
      @argv = ['foo', 4]
    end

    def test_run_success
      assert_output("348\n") { ::CalculatorCliApp::Application.run!(argv) }
    end

    private

    attr_reader :argv
  end
end
