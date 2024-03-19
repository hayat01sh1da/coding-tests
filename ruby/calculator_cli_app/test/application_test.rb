require 'minitest/autorun'
require_relative '../src/application'

class CalculatorCliApp::ApplicationTest < Minitest::Test
  def setup
    argv = ['foo', 4]
    @app = ::CalculatorCliApp::Application.new(argv)
  end

  def test_run_success
    assert_output("348\n") { @app.run }
  end
end
