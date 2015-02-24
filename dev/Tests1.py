'''
Created on Feb 23, 2015

@author: kguschina
'''
import unittest


class Test(unittest.TestCase):


    def test1(self):
        pass
    
    def test2(self):
        pass
    
    def test3(self):
        self.assertEqual(2, 3)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()