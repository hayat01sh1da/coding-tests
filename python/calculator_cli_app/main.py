from application import Application
import sys
import os
import shutil
import glob
sys.path.append('./calculator_cli_app/src')

sys.argv.pop(0)
app = Application(args=sys.argv)
app.run()

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive=True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
