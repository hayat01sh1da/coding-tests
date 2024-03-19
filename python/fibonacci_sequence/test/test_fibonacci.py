import unittest
import sys
sys.path.append('./src')
from fibonacci import *

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            fibonacci(0, 10)
        )

    def test_fibonacci_2(self):
        self.assertEqual(
            [10, 11, 21, 32, 53, 85, 138, 223, 361, 584],
            fibonacci(10, 10)
        )

if __name__ == '__main__':
    unittest.main()
