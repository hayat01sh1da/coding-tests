import unittest
import sys
import glob
import os
import shutil
sys.path.append('./src')
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
