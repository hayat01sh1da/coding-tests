import unittest
import sys
sys.path.append('./src')
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_in_if(self):
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                self.assertEqual('FizzBuzz', fizzbuzz_in_if(num))
            elif num % 3 == 0:
                self.assertEqual('Fizz', fizzbuzz_in_if(num))
            elif num % 5 == 0:
                self.assertEqual('Buzz', fizzbuzz_in_if(num))
            else:
                self.assertEqual(str(num), fizzbuzz_in_if(num))

    def test_fizzbuzz_in_ternary(self):
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
