import unittest
import sys
from io import StringIO
import glob
import os
import shutil

# Add src paths relative to this test file's location
test_dir    = os.path.dirname(os.path.abspath(__file__))
module_root = os.path.dirname(os.path.dirname(test_dir))
src_paths   = [
    os.path.join(module_root, 'src', 'queries'),
    os.path.join(module_root, 'src')
]
for src_path in src_paths:
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

from calculation_query import CalculationQuery

class TestCalculationQuery(unittest.TestCase):
    def setUp(self):
        self.calculation_query = CalculationQuery('foo')
        self.org_stdout        = sys.stdout
        sys.stdout             = StringIO()
        self.pycaches          = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def tearDown(self):
        sys.stdout = self.org_stdout
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

class TestArgumentZero(TestCalculationQuery):
    def test_f_with_zero(self):
        self.assertEqual(self.calculation_query.f(0), 1)

class TestArgumentTwo(TestCalculationQuery):
    def test_f_with_two(self):
        self.assertEqual(self.calculation_query.f(2), 2)

class TestArgumentFour(TestCalculationQuery):
    def test_f_with_four(self):
        self.assertEqual(self.calculation_query.f(4), 348)

if __name__ == '__main__':
    unittest.main()
