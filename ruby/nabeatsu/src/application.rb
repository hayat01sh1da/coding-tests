def go_crazy_in_if(num)
  if (num % 3).zero? || num.to_s.include?('3')
    # Express the status of "crazy" with '!'
    "#{num}!"
  else
    num.to_s
  end
end

def go_crazy_in_ternary(num)
  # Express the status of "crazy" with '!'
  (num % 3).zero? || num.to_s.include?('3') ? "#{num}!" : num.to_s
end
