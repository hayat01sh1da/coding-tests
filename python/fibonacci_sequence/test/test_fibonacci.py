import unittest
import sys
import glob
import os
import shutil

# Add src path relative to this test file's location
test_dir    = os.path.dirname(os.path.abspath(__file__))
module_root = os.path.dirname(test_dir)
src_path    = os.path.join(module_root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from fibonacci import *

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def tearDown(self):
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

class TestCase1(TestFibonacci):
    def test_fibonacci(self):
        self.assertEqual(
            fibonacci(0, 10),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        )

class TestCase2(TestFibonacci):
    def test_fibonacci(self):
        self.assertEqual(
            fibonacci(10, 10),
            [10, 11, 21, 32, 53, 85, 138, 223, 361, 584]
        )

if __name__ == '__main__':
    unittest.main()
