import sys
import os
import shutil
import glob
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

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.isdir(pycache):
        shutil.rmtree(pycache)
