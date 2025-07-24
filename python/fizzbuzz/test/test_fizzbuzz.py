import unittest
import sys
import glob
import os
import shutil
sys.path.append('./src')
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def tearDown(self):
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

class TestIfStatement(TestFizzBuzz):
    def test_fizzbuzz(self):
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                self.assertEqual(fizzbuzz_in_if(num), 'FizzBuzz')
            elif num % 3 == 0:
                self.assertEqual(fizzbuzz_in_if(num), 'Fizz')
            elif num % 5 == 0:
                self.assertEqual(fizzbuzz_in_if(num), 'Buzz')
            else:
                self.assertEqual(fizzbuzz_in_if(num), str(num))

class TestTernaryStatement(TestFizzBuzz):
    def test_fizzbuzz(self):
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                self.assertEqual(fizzbuzz_in_ternary(num), 'FizzBuzz')
            elif num % 3 == 0:
                self.assertEqual(fizzbuzz_in_ternary(num), 'Fizz')
            elif num % 5 == 0:
                self.assertEqual(fizzbuzz_in_ternary(num), 'Buzz')
            else:
                self.assertEqual(fizzbuzz_in_ternary(num), str(num))

if __name__ == '__main__':
    unittest.main()
