import unittest
import sys
import glob
import os
import shutil
sys.path.append('./src')
from nabeatsu import *

class TestNabeatsu(unittest.TestCase):
    def setUp(self):
        self.pycaches = glob.glob(os.path.join('.', '**', '__pycache__'))

    def tearDown(self):
        for pycache in self.pycaches:
            if os.path.isdir(pycache):
                shutil.rmtree(pycache)

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
