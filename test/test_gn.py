'''
GotoNewest tests
'''

import unittest
import sys
sys.path.append('../src/')
import gn

TEST_DIR_NO_SUB = '/tmp/testnosub'
TEST_DIR_ONE_SUB = '/tmp/testonesub'
TEST_DIR_TWO_SUB = '/tmp/testtwosub'

class TestGotoNewest(unittest.TestCase):
    ''' Test class for GotoNewest
    '''

    def test_empty_base_dir(self):
        ''' If the base directory is empty, raise an
        AttributeError
        '''
        self.assertRaises(AttributeError, gn.transfer, None)

    def test_base_dir_with_no_subdirs(self):
        ''' If the base directory has no subdirectories,
        raise an AttributeError
        '''
        self.assertRaises(AttributeError, gn.transfer, TEST_DIR_NO_SUB)

    def test_one_subdirectory(self):
        ''' If there is only one subdirectory in the base
        directory, return the directory
        '''
        self.assertEquals('temp', gn.transfer(TEST_DIR_ONE_SUB))

    def test_multiple_subdirectories(self):
        ''' If there are multiple subdirectories in the base
        directory, find the one created most recently and
        return it
        '''
        self.assertEquals('temp2', gn.transfer(TEST_DIR_TWO_SUB))


if __name__ == '__main__':
    unittest.main()
