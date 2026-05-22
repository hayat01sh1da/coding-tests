import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_HERE, 'src'))

from application import fibonacci  # noqa: E402

print('Provide the initial number to start the sequence from')
init_num_input = input().strip()

print('Provide the number of iterations')
iter_input = input().strip()

params: dict[str, int] = {}
if init_num_input:
    params['init_num'] = int(init_num_input)
if iter_input:
    params['iter'] = int(iter_input)

print(', '.join(str(n) for n in fibonacci(**params)))
