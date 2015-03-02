import unittest
import sys
sys.path.append('../src/')
import gn

class TestGotoNewest(unittest.TestCase):

    def test_empty_base_dir_raises_error(self):
        self.assertRaises(AttributeError, gn.transfer, None)


if __name__ == '__main__':
    unittest.main()
