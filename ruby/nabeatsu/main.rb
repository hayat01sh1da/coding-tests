require_relative './src/nabeatsu'

result_1 = Array.new
result_2 = Array.new

1.upto(40).each do |num|
  result_1.push(go_crazy_in_if(num))
  result_2.push(go_crazy_in_ternary(num))
end

p result_1
p result_2
