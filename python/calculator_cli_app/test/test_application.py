import unittest
import sys
from io import StringIO
sys.path.append('./src')
sys.path.append('./src/lib')
sys.path.append('./src/queries')
sys.path.append('./src/validations')
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.org_stdout = sys.stdout
        sys.stdout      = StringIO()
        argv            = ['foo', 4]
        self.app        = Application(argv)

    def test_run_success(self):
        self.app.run()
        self.assertEqual('348\n', sys.stdout.getvalue())

    def tearDown(self):
        sys.stdout = self.org_stdout

if __name__ == '__main__':
    unittest.main()
