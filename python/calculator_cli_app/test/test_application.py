from application import Application
import unittest
import sys
from io import StringIO
import glob
import os
import shutil

# Add src paths relative to this test file's location
test_dir = os.path.dirname(os.path.abspath(__file__))
module_root = os.path.dirname(test_dir)
src_paths = [
    os.path.join(module_root, 'src'),
    os.path.join(module_root, 'src', 'lib'),
    os.path.join(module_root, 'src', 'queries'),
    os.path.join(module_root, 'src', 'validations')
]

# Remove cached modules to ensure fresh import
for module in list(sys.modules.keys()):
    if module in [
        'application',
        'data_type_conversion',
        'calculation_query',
            'args_validation']:
        del sys.modules[module]

for src_path in src_paths:
    if src_path not in sys.path:
        sys.path.insert(0, src_path)


class TestApplication(unittest.TestCase):
    def setUp(self):
        self.org_stdout = sys.stdout
        sys.stdout = StringIO()
        argv = ['foo', 4]
        self.app = Application(args=argv)
        self.pycaches = glob.glob(
            os.path.join(
                '.',
                '**',
                '__pycache__'),
            recursive=True)

    def test_run_success(self):
        self.app.run()
        self.assertEqual(sys.stdout.getvalue(), '348\n')

    def tearDown(self):
        sys.stdout = self.org_stdout
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)


if __name__ == '__main__':
    unittest.main()
