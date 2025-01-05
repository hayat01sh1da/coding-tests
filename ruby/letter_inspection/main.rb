require_relative './src/application'

str_1     = 'hogefoobar'
str_2     = 'abefghooor'
str_3     = 'hoge'
str_4     = 'piyopoopee'
pattern_1 = LetterInspection::Application.new(str_1, str_2)
pattern_2 = LetterInspection::Application.new(str_1, str_3)
pattern_3 = LetterInspection::Application.new(str_1, str_4)

p patternit.exactly_equal_size_and_included?
p pattern_2.exactly_equal_size_and_included?
p pattern_3.exactly_equal_size_and_included?
