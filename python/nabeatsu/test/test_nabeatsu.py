import unittest
import sys
import glob
import os
import shutil
sys.path.append('./src')
from nabeatsu import *

class TestNabeatsu(unittest.TestCase):
    def setUp(self):
        self.pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def tearDown(self):
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

class TestIfStatement(TestNabeatsu):
    def test_go_crazy(self):
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                self.assertEqual(go_crazy_in_if(num), str(num) + '!')
            else:
                self.assertEqual(go_crazy_in_if(num), str(num))

class TestTernaryStatement(TestNabeatsu):
    def test_go_crazy(self):
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                self.assertEqual(go_crazy_in_ternary(num), str(num) + '!')
            else:
                self.assertEqual(go_crazy_in_ternary(num), str(num))

if __name__ == '__main__':
    unittest.main()
