require_relative './src/fizzbuzz'

result_1 = Array.new
result_2 = Array.new
result_3 = Array.new

1.upto(100).each do |num|
  resultit.push(fizzbuzz_in_if(num))
  result_2.push(fizzbuzz_in_if_and_ternary(num))
  result_3.push(fizzbuzz_in_ternary(num))
end

p result_1
p result_2
p result_3
