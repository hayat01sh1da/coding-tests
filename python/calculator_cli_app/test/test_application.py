import unittest
import sys
from io import StringIO
import glob
import os
import shutil
sys.path.append('./src')
sys.path.append('./src/lib')
sys.path.append('./src/queries')
sys.path.append('./src/validations')
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self) -> None:
        self.org_stdout = sys.stdout
        sys.stdout      = StringIO()
        argv            = ['foo', 4]
        self.app        = Application(args = argv)
        self.pycaches   = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def test_run_success(self) -> None:
        self.app.run()
        self.assertEqual(sys.stdout.getvalue(), '348\n')

    def tearDown(self) -> None:
        sys.stdout = self.org_stdout
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

if __name__ == '__main__':
    unittest.main()
