import unittest
import glob
import os
import shutil
from application import Application


class TestApplication(unittest.TestCase):
    def setUp(self):
        str_1 = 'hogefoobar'
        str_2 = 'abefghooor'
        str_3 = 'hoge'
        str_4 = 'piyopoopee'
        self.pattern_1 = Application(str_1=str_1, str_2=str_2)
        self.pattern_2 = Application(str_1=str_1, str_2=str_3)
        self.pattern_3 = Application(str_1=str_1, str_2=str_4)
        test_dir = os.path.dirname(os.path.abspath(__file__))
        module_root = os.path.dirname(test_dir)
        self.pycaches = glob.glob(
            os.path.join(
                module_root,
                '**',
                '__pycache__'),
            recursive=True)

    def tearDown(self):
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)


class TestRegularCase(TestApplication):
    def test_exactly_equal_size_and_included_1(self):
        self.assertTrue(self.pattern_1.exactly_equal_size_and_included())


class TestIrregularCase(TestApplication):
    pass


class TestCase1(TestIrregularCase):
    def test_exactly_equal_size_and_included_2(self):
        self.assertFalse(self.pattern_2.exactly_equal_size_and_included())


class TestCase1(TestIrregularCase):
    def test_exactly_equal_size_and_included_3(self):
        self.assertFalse(self.pattern_3.exactly_equal_size_and_included())


if __name__ == '__main__':
    unittest.main()
