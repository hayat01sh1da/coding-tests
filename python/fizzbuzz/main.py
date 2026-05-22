import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_HERE, 'src'))

from application import (  # noqa: E402
    fizzbuzz_in_if,
    fizzbuzz_in_if_and_ternary,
    fizzbuzz_in_ternary,
)

print('Provide the initial number to start the sequence from')
init_num = int(input().strip())

print('Provide the terminal number of stop the sequence at')
terminal_num = int(input().strip())

print('Which logic do you want to use? (1: if, 2: if and ternary, 3: ternary)')
logic_type = int(input().strip())

result: list[str] = []
for num in range(init_num, terminal_num + 1):
    if logic_type == 1:
        result.append(fizzbuzz_in_if(num))
    elif logic_type == 2:
        result.append(fizzbuzz_in_if_and_ternary(num))
    elif logic_type == 3:
        result.append(fizzbuzz_in_ternary(num))
    else:
        result.append(str(num))

print(', '.join(result))
