# rbs_inline: enabled

# @rbs init_num: Integer
# @rbs iter: Integer
# @rbs return: Array[Integer]
def fibonacci(init_num:, iter:)
  current_num = init_num
  next_num    = current_num + 1
  Array.new(iter) do
    result_num            = current_num
    current_num, next_num = next_num, current_num + next_num
    result_num
  end
end
