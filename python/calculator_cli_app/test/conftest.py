import os
import sys

_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(_SRC)
sys.path.append(os.path.join(_SRC, 'queries'))
sys.path.append(os.path.join(_SRC, 'validations'))
