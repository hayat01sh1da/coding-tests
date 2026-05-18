from fibonacci import fibonacci
import sys
import os
import shutil
import glob
sys.path.append('./fibonacci/src')

print(fibonacci(0, 20))

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive=True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
