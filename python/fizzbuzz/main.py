import sys
sys.path.append('./fizzbuzz/src')
from fizzbuzz import *

result_1 = list()
result_2 = list()

for i in range(1, 101):
    result_1.append(fizzbuzz_in_if(i))

for i in range(1, 101):
    result_2.append(fizzbuzz_in_ternary(i))

print(result_1)
print(result_2)
