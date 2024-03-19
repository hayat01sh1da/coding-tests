import sys
sys.path.append('./letter_inspection/src')
from application import Application

str_1     = 'hogefoobar'
str_2     = 'abefghooor'
str_3     = 'hoge'
str_4     = 'piyopoopee'
pattern_1 = Application(str_1, str_2)
pattern_2 = Application(str_1, str_3)
pattern_3 = Application(str_1, str_4)

print(pattern_1.exactly_equal_size_and_included())
print(pattern_2.exactly_equal_size_and_included())
print(pattern_3.exactly_equal_size_and_included())
