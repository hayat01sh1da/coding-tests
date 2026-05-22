import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_HERE, 'src'))

from application import Application  # noqa: E402

print('Provide the source string to compare from')
source = input().strip()

print('Provide the target string to compare with')
target = input().strip()

result = Application.exactly_equal_size_and_included(
    source=source, target=target)
print(f'Result: {str(result).lower()}')
