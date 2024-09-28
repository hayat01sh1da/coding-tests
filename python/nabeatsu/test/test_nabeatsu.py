import unittest
import sys
sys.path.append('./src')
from nabeatsu import *

class TestNabeatsu(unittest.TestCase):
    pass

class TestIfStatement(TestNabeatsu):
    def test_go_crazy(self):
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                self.assertEqual(str(num) + '!', go_crazy_in_if(num))
            else:
                self.assertEqual(str(num), go_crazy_in_if(num))

class TestTernaryStatement(TestNabeatsu):
    def test_go_crazy(self):
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                self.assertEqual(str(num) + '!', go_crazy_in_ternary(num))
            else:
                self.assertEqual(str(num), go_crazy_in_ternary(num))

if __name__ == '__main__':
    unittest.main()
