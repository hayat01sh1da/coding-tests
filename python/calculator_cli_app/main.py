import sys
sys.path.append('./calculator_cli_app/src')
from application import Application

sys.argv.pop(0)
app = Application(sys.argv)
app.run()
