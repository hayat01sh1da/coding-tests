import sys
import os
import shutil
import glob
sys.path.append('./fibonacci/src')
from fibonacci import *

print(fibonacci(0, 20))

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
