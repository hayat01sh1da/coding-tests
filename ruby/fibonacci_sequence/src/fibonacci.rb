# rbs_inline: enabled

# @rbs init_num: Integer
# @rbs iter: Integer
# @rbs return: Array[Integer]
def fibonacci(init_num:, iter:)
  current_num = init_num
  next_num    = current_num + 1
  result      = Array.new
  iter.times do
    result.push(current_num)
    current_num, next_num = next_num, current_num + next_num
  end
  result
end
