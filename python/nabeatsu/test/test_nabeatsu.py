import unittest
import sys
sys.path.append('./src')
from nabeatsu import *

class TestNabeatsu(unittest.TestCase):
    def test_go_crazy_in_if(self):
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                self.assertEqual(str(num) + '!', go_crazy_in_if(num))
            else:
                self.assertEqual(str(num), go_crazy_in_if(num))

    def test_go_crazy_in_ternary(self):
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                self.assertEqual(str(num) + '!', go_crazy_in_ternary(num))
            else:
                self.assertEqual(str(num), go_crazy_in_ternary(num))

if __name__ == '__main__':
    unittest.main()
