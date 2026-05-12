require 'minitest/autorun'
require_relative '../src/application'

class CalculatorCliApp::ApplicationTest < Minitest::Test
  def setup
    @argv = ['foo', 4]
  end

  def test_run_success
    assert_output("348\n") { ::CalculatorCliApp::Application.run!(argv) }
  end

  private

  attr_reader :argv
end
