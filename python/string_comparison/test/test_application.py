import unittest
import sys
sys.path.append('./src')
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        str_1          = 'hogefoobar'
        str_2          = 'abefghooor'
        str_3          = 'hoge'
        str_4          = 'piyopoopee'
        self.pattern_1 = Application(str_1, str_2)
        self.pattern_2 = Application(str_1, str_3)
        self.pattern_3 = Application(str_1, str_4)

    def test_exactly_equal_size_and_included_1(self):
        self.assertEqual(True, self.pattern_1.exactly_equal_size_and_included())

    def test_exactly_equal_size_and_included_2(self):
        self.assertEqual(False, self.pattern_2.exactly_equal_size_and_included())

    def test_exactly_equal_size_and_included_3(self):
        self.assertEqual(False, self.pattern_3.exactly_equal_size_and_included())

if __name__ == '__main__':
    unittest.main()
