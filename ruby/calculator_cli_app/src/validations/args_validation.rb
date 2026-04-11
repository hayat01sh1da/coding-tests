# rbs_inline: enabled

module Validations
  module ArgsValidation
    # @rbs args_size: Integer
    # @rbs seed: String
    # @rbs n: Integer?
    # @rbs return: void
    def validate!(args_size, seed, n)
      if args_size > 2
        puts 'Too many arguments'
        exit 1
      elsif args_size == 0
        puts 'No argument provided'
        exit 1
      elsif args_size == 1
        puts 'Provide both seed and n'
        exit 1
      elsif !seed.instance_of?(String) || n.nil?
        puts 'Provide seed as string and n as number'
        exit 1
      end
    end
  end
end
