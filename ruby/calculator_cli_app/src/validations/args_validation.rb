# frozen_string_literal: true
# rbs_inline: enabled

module Validations
  # Argument-shape checks for CalculatorCliApp::Application.
  module ArgsValidation
    # @rbs args_size: Integer
    # @rbs seed: String
    # @rbs num: Integer?
    # @rbs return: void
    def validate!(args_size, seed, num)
      message = validation_error(args_size, seed, num)
      return unless message

      puts message
      exit 1
    end

    private

    # @rbs args_size: Integer
    # @rbs seed: String
    # @rbs num: Integer?
    # @rbs return: String?
    def validation_error(args_size, seed, num)
      return 'Too many arguments'                     if args_size > 2
      return 'No argument provided'                   if args_size.zero?
      return 'Provide both seed and n'                if args_size == 1
      return 'Provide seed as string and n as number' if !seed.instance_of?(String) || num.nil?

      nil
    end
  end
end
