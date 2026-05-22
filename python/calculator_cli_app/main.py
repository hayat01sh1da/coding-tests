import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_HERE, 'src'))
sys.path.append(os.path.join(_HERE, 'src', 'queries'))
sys.path.append(os.path.join(_HERE, 'src', 'validations'))

from application import Application  # noqa: E402

sys.argv.pop(0)
Application.run(args=sys.argv)
