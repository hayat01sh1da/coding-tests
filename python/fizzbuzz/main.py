import sys
import os
import shutil
import glob
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

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
