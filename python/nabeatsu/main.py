import sys
sys.path.append('./nabeatsu/src')
from nabeatsu import *

result_1 = list()
result_2 = list()

for i in range(1, 41):
    result_1.append(go_crazy_in_if(i))

for i in range(1, 41):
    result_2.append(go_crazy_in_ternary(i))

print(result_1)
print(result_2)
