# frozen_string_literal: true
# rbs_inline: enabled

# @rbs num: Integer
# @rbs return: String
def fizzbuzz_in_if(num)
  if (num % 3).zero? && (num % 5).zero?
    'FizzBuzz'
  elsif (num % 3).zero?
    'Fizz'
  elsif (num % 5).zero?
    'Buzz'
  else
    num.to_s
  end
end

# @rbs num: Integer
# @rbs return: String
def fizzbuzz_in_if_and_ternary(num)
  if (num % 3).zero?
    (num % 5).zero? ? 'FizzBuzz' : 'Fizz'
  else
    (num % 5).zero? ? 'Buzz' : num.to_s
  end
end

# @rbs num: Integer
# @rbs return: String
def fizzbuzz_in_ternary(num)
  if (num % 3).zero?
    (num % 5).zero? ? 'FizzBuzz' : 'Fizz'
  else
    (num % 5).zero? ? 'Buzz' : num.to_s
  end
end
