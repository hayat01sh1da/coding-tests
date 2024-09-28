import unittest
import sys
sys.path.append('./src')
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    pass

class TestIfStatement(TestFizzBuzz):
    def test_fizzbuzz(self):
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                self.assertEqual('FizzBuzz', fizzbuzz_in_if(num))
            elif num % 3 == 0:
                self.assertEqual('Fizz', fizzbuzz_in_if(num))
            elif num % 5 == 0:
                self.assertEqual('Buzz', fizzbuzz_in_if(num))
            else:
                self.assertEqual(str(num), fizzbuzz_in_if(num))

class TestTernaryStatement(TestFizzBuzz):
    def test_fizzbuzz(self):
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                self.assertEqual('FizzBuzz', fizzbuzz_in_ternary(num))
            elif num % 3 == 0:
                self.assertEqual('Fizz', fizzbuzz_in_ternary(num))
            elif num % 5 == 0:
                self.assertEqual('Buzz', fizzbuzz_in_ternary(num))
            else:
                self.assertEqual(str(num), fizzbuzz_in_ternary(num))

if __name__ == '__main__':
    unittest.main()
