require_relative './src/application'

app = ::CalculatorCliApp::Application.new(ARGV)
app.run
