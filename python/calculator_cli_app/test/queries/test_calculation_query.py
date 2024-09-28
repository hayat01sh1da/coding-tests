import unittest
import sys
sys.path.append('./src/queries')
from calculation_query import CalculationQuery

class TestCalculationQuery(unittest.TestCase):
  def setUp(self):
    self.calculation_query = CalculationQuery('foo')

class TestArgumentZero(TestCalculationQuery):
  def test_f_with_zero(self):
    self.assertEqual(1, self.calculation_query.f(0))

class TestArgumentTwo(TestCalculationQuery):
  def test_f_with_two(self):
    self.assertEqual(2, self.calculation_query.f(2))

class TestArgumentFour(TestCalculationQuery):
  def test_f_with_four(self):
    self.assertEqual(348, self.calculation_query.f(4))

if __name__ == '__main__':
    unittest.main()
