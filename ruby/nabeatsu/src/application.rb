def go_crazy_in_if(num)
  if num % 3 == 0 || num.to_s.include?('3')
    # Express the status of "crazy" with '!'
    "#{num.to_s}!"
  else
    num.to_s
  end
end

def go_crazy_in_ternary(num)
  # Express the status of "crazy" with '!'
  num % 3 == 0 || num.to_s.include?('3') ? "#{num.to_s}!" : num.to_s
end
