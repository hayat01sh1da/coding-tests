import unittest
import sys
import glob
import os
import shutil

# Add src path relative to this test file's location
test_dir = os.path.dirname(os.path.abspath(__file__))
module_root = os.path.dirname(test_dir)
src_path = os.path.join(module_root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

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
